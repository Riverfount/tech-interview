import json

from django.http import JsonResponse

from .rules import build_carts


def level1(request):
    """
    This view receives request with a payload with articles and carts and responds with a JSON with carts with total
    price.
    """
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


def level2(request):
    """
    This view receives request with a payload with articles, carts, and delivery fees and responds with a JSON with
    carts with total price using the policy of delivery fees.
    """
    try:
        data = json.loads(request.body.decode('utf-8'))
        if not data:
            raise ValueError
        response = build_carts(data['articles'], data['carts'], data['delivery_fees'])
    except KeyError as err:
        args = err.args
        response = [{"Error": {"Message": f"The follow keys {args} were not present on payload."}}]
    except ValueError:
        response = [{"Error": {"Message": "The payload is not present on the request."}}]
    return JsonResponse(response, safe=False)


def level3(request):
    """
    This view receives request with a payload with articles, carts, delivery fees, and discounts and responds with a
    JSON with carts with total price using the policy of delivery fees and the discounts if applicable.
    """
    try:
        data = json.loads(request.body.decode('utf-8'))
        if not data:
            raise ValueError
        response = build_carts(data['articles'], data['carts'], data['delivery_fees'], data['discounts'])
    except KeyError as err:
        args = err.args
        response = [{"Error": {"Message": f"The follow keys {args} were not present on payload."}}]
    except ValueError:
        response = [{"Error": {"Message": "The payload is not present on the request."}}]
    return JsonResponse(response, safe=False)
