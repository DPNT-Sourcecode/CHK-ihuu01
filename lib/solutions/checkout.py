from collections import Counter

ITEMS = {
    'A': {'price': 50, 'special_offers': [{'min_quantity': 3, 'price': 130},
                                          {'min_quantity': 5, 'price': 200}]},
    'B': {'price': 30, 'special_offers': [{'min_quantity': 2, 'price': 45}]},
    'C': {'price': 20, 'special_offers': []},
    'D': {'price': 15, 'special_offers': []},
    'E': {'price': 40, 'special_offers': [{'min_quantity': 2, 'other_free': 'B'}]}
}

# 'AAA' 50, 100, 150 (should be 130) so minus 20 at end?
# 'AAAAAAAAA' (9as) 200 + 130 + 50

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
                number_of_offers = qty // offer['min_quantity']

                # how many are left, put in qty for next offer...
                number_of_items_in_offer = number_of_offers * offer['min_quantity']
                qty -= number_of_items_in_offer

                # update the line total
                line_total += number_of_offers * offer['price']

            elif 'other_free' in offer:
                if offer['other_free'] in skus:
                    other_free = offer['other_free']
                    free_offer = ITEMS[other_free]['price']

        # add any remaining qty as full price to the line_total
        line_total += qty * ITEMS[item]['price']

        # add the line total, and the free offers to the checkout total
        total += line_total
        total -= free_offer

    return total
