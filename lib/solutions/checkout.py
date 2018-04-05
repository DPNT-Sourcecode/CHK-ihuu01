from collections import Counter

ITEMS = {
    'A': {'price': 50, 'special_offers': [(3, -20), (5, -50)]},
    'B': {'price': 30, 'special_offers': [(2, -15)]},
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
    special_counter = Counter(skus)

    for item in skus:
        if item in ITEMS:
            # increment the total
            total += ITEMS[item]['price']
        else:
            return -1

    # now check the special offers
    for item in special_counter:
        # does this item have an specials?
        if 'special_offers' in ITEMS[item]:
            required_quantity, discount = ITEMS[item]['special_offers']

            number_of_discounts = special_counter[item] // required_quantity
            total += (discount * number_of_discounts)

    return total
