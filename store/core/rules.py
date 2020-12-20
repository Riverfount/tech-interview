def get_price(cod: int, articles: list) -> int:
    return [p['price'] for p in articles if p['id'] == cod][0]


# Following is the code with the Busines Rules of the Level 1


def build_carts(articles: list, carts: list) -> list[list]:
    total_item = 0
    total_cart = 0
    carts_restul = []
    for cart in carts:
        for item in cart['items']:
            total_item = get_price(item['article_id'], articles) * item['quantity']
            total_cart += total_item
        carts_restul.append({'id': cart['id'], 'total': total_cart})
        total_item = 0
        total_cart = 0
    resutl = {"carts": carts_restul}
    return resutl
