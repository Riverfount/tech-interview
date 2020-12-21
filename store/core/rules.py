"""
This module has the functions to apply the Business Rules of the Store.

The Business Rules are:

    * The customer is charged the sum of the prices of each article in their cart.
        In the function build_carts we calculate the sum of the prices of each article in their cart.
        To do this we use the auxiliary function get_price.
    * Cost of delivery depends on how much we charged the customer for the contents of their carts. The more the
      customer spends, the less they are charged for shipping.
        The delivery fee is calculated in the build_carts. Special attention to the 'if statement' of it, because the
        last pair of information about the minimum and maximum price to give a delivery fee for free is 2000 as a
        minimum and null as a maximum, but null it is not a number. So, we apply a float('inf') to define the maximum
        like an infinitum. Works Good!!!
    * Some products are discounted because of a deal we made with the supplier.
        In addition to the function get_price, we put the optional because it is not all articles that have a discount,
        it is simple 'for statement' to get, if applicable, the discount of the article.
"""


def get_price(cod: int, articles: list, discounts: list = None) -> int:
    """
    Returns the price of a specific article from a given list.

    Parameters:
        cod: An integer that means the article id. This parameter is mandatory.
        article: A list of articles with all articles and their prices. This parameter is mandatory.
        discounts: A list of discounts if applicable. This parameter is optional.

    Returns:
        price: Price of the article and if applicable with its discount.
    """

    price = [p['price'] for p in articles if p['id'] == cod][0]
    type = ''
    value = 0
    if discounts:
        for discount in discounts:
            if discount['article_id'] == cod:
                value = discount['value']
                type = discount['type']
        price = price - value if type == 'amount' else int(price - (price * value / 100))
    return price


def build_carts(articles: list, carts: list, delivery_fees: list = None, discounts: list = None) -> list:
    """
    Returns a list of carts with the prices of all its articles totalized.

    Parameters:
        articles: A list with all articles. This parameter is mandatory.
        carts: A list of carts with their articles and their quantities. This parameter is mandatory.
        delivery_fees: A list of delivery fees if applicable. This parameter is optional.
        discounts: A list of discounts if applicable. This parameter is optional.

    Returns:
        carts: A list of carts with their id and total price.
    """
    total_item = 0
    total_cart = 0
    delivery_value = 0
    carts_restul = []
    for cart in carts:
        for item in cart['items']:
            total_item = get_price(item['article_id'], articles, discounts) * item['quantity']
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
