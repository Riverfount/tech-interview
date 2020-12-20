import json

from django.http import JsonResponse

from .rules import build_carts


def level1(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        if not data:
            raise ValueError
        response = build_carts(data['articles'], data['carts'])
    except KeyError as err:
        args = err.args
        response = [{"Error": {"Message": f"The follow keys {args} were not present on payload."}}]
    except ValueError:
        response = [{"Error": {"Message": "The payload is not present on the request."}}]

    return JsonResponse(response, safe=False)
