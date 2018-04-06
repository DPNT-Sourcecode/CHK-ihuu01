from collections import Counter

ITEMS = {
    'A': {'price': 50, 'special_offers': [{'min_quantity': 3, 'price': 200},
                                          {'min_quantity': 5, 'price': 130}]},
    'B': {'price': 30, 'special_offers': [{'min_quantity': 2, 'price': 45}]},
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
    counter = Counter(skus)

    # got through the offers (biggest first), and calculate the line total, and any free offers...
    for item in counter:
        if item not in ITEMS:
            return -1

        line_total = 0
        free_offer = 0
        qty = counter[item]

        ordered_offers = sorted(ITEMS[item]['special_offers'], key=lambda k: (k['min_quantity']), reverse=True)

        # does this item have an specials?
        for offer in ordered_offers:

            if 'price' in offer:
                # how many can we get of the biggest offer
                number_of_discounts = qty // offer['min_quantity']

                # how many are left...

            #


            elif 'other_free' in offer:
                if offer['other_free'] in skus:
                    other_free = offer['other_free']
                    free_offer = total - ITEMS[other_free]['price']

        # add the line total, and the free offers to the checkout total
        total += line_total
        total -= free_offer

    return total
