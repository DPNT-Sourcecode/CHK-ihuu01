from collections import Counter

ITEMS = {
    'A': {'price': 50, 'special_offers': [{'min_quantity': 3, 'discount': -20},
                                          {'min_quantity': 5, 'discount': -30}]},
    'B': {'price': 30, 'special_offers': [{'min_quantity': 2, 'discount': -15}]},
    'C': {'price': 20, 'special_offers': []},
    'D': {'price': 15, 'special_offers': []},
    'E': {'price': 40, 'special_offers': [{'min_quantity': 2, 'other_free': 'B'}]}
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
        for offer in ITEMS[item]['special_offers']:
            number_of_discounts = special_counter[item] // offer['min_quantity']

            if 'discount' in offer:
                total += (offer['discount'] * number_of_discounts)

            elif 'other_free' in offer:
                if offer['other_free'] in skus:
                    other_free = ITEMS[item]['other_free']
                    total = total - ITEMS[other_free]['price']

    return total
