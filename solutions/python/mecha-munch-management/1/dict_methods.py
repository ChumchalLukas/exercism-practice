"""Functions to manage a users shopping cart items."""
from collections import OrderedDict

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for cart_item in items_to_add:
        if cart_item in list(current_cart.keys()):
            current_cart[cart_item] += 1
        else:
            current_cart[cart_item] = 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """


    # creating dictionary - no duplicates
    if len(set(notes)) == len(notes):
        return dict.fromkeys(notes, 1)
    
    # creating dictionary - duplicates
    notes_cart = {}

    for item in notes:
        if item not in notes_cart.keys():
            notes_cart[item] = 1
        else:
            notes_cart[item] += 1

    return notes_cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    # Main data copy
    updated_ideas = ideas.copy()
    
    # Updating
    for recipe_name, new_ingredients in recipe_updates:
        updated_ideas[recipe_name] = new_ingredients
    
    return updated_ideas





def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    # Sort elements:
    cart_copy = dict(sorted(cart.copy().items(), reverse=True))
    aisle_copy = dict(sorted(aisle_mapping.copy().items(), reverse=True))
    

    for key_word, value_word in aisle_copy.items():
        if key_word in cart_copy:
            if not isinstance(cart_copy[key_word], list):
                cart_copy[key_word] = [cart_copy[key_word]]
            cart_copy[key_word].extend(value_word)
            
    return cart_copy
    

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.
    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    # Data copy:
    fulfillment_cart_copy = fulfillment_cart.copy()
    store_inventory_copy = store_inventory.copy()
    
    for keyword in fulfillment_cart_copy:
        changed_store_item = fulfillment_cart_copy[keyword][0]
        store_inventory_copy[keyword][0] -= changed_store_item
        
        if store_inventory_copy[keyword][0] == 0:
            store_inventory_copy[keyword][0] = 'Out of Stock'
   
    return store_inventory_copy

