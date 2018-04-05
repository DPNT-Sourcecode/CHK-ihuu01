
ITEMS = {
    'A': {'price': 50, 'special_offers': (3, 30)},
    'B': {'price': 30, 'special_offers': (2, 45)},
    'C': {'price': 20},
    'D': {'price': 15}
}

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    """
    Calculate the total amount for the checkout based on the SKUs entered in

    :param skus: string, each char is an item
    :return: int, total amount of the cart, including special offers
    """
    total = 0

    for item in skus:
        if item in ITEMS:
            # check for special offers
            # if 'special_offers' in ITEMS[item]:
            #     quantity_required,

            # increment the total
            total += ITEMS[item]['price']

        else:
            return -1

    return total