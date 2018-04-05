from collections import defaultdict

ITEMS = {
    'A': {'price': 50, 'special_offers': (3, 130)},
    'B': {'price': 30, 'special_offers': (2, 45)},
    'C': {'price': 20},
    'D': {'price': 15}
}

# 'AAA' 50, 100, 150 (should be 130) so minus 20 at end?

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    """
    Calculate the total amount for the checkout based on the SKUs entered in

    :param skus: string, each char is an item
    :return: int, total amount of the cart, including special offers
    """
    total = 0
    special_counter = defaultdict(int)

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
