from typing import Dict


def get_price(cod: int, articles: list) -> int:
    return [p['price'] for p in articles if p['id'] == cod][0]


# Following is the code with the Busines Rules of the Level 1


def build_carts(articles: list, carts: list, delivery_fees: Dict = None) -> list[list]:
    total_item = 0
    total_cart = 0
    delivery_value = 0
    carts_restul = []
    for cart in carts:
        for item in cart['items']:
            total_item = get_price(item['article_id'], articles) * item['quantity']
            total_cart += total_item
        if delivery_fees:
            for delivery_fee in delivery_fees:
                if (total_cart >= delivery_fee['eligible_transaction_volume']['min_price']) or (
                    total_cart
                    > (
                        float('inf')
                        if not delivery_fee['eligible_transaction_volume']['max_price']
                        else delivery_fee['eligible_transaction_volume']['max_price']
                    )
                ):
                    delivery_value = delivery_fee['price']
        carts_restul.append({'id': cart['id'], 'total': total_cart + delivery_value})
        total_item = 0
        total_cart = 0
    resutl = {"carts": carts_restul}
    return resutl
