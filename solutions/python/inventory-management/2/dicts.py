"""Functions to keep track and alter inventory."""

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.
    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory_ready = {}
    for tool in set(items):
        inventory_ready[tool] = items.count(tool)
    return inventory_ready

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    items_inventory = create_inventory(items)  # gear update
    for tool in items_inventory:
        if tool in inventory:
            inventory[tool] += items_inventory[tool]
        else:
            inventory[tool] = items_inventory[tool]
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.
    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    items_inventory = create_inventory(items)  # Get count of items to remove
    for tool in items_inventory:
        if tool in inventory:  # Only modify existing items
            inventory[tool] -= items_inventory[tool]
            if inventory[tool] < 0:
                inventory[tool] = 0
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory
    
def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(key, value) for key, value in inventory.items() if value > 0]