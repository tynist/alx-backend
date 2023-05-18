#!/usr/bin/python3
"""
MRU Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class that represents a caching system using the MRU algo"""


    def __init__(self):
        """Initialize the MRUCache."""
        super().__init__()
        self.mru_order = OrderedDict()

    def put(self, key, item):
        """Assigns the item value to the key in the cache using the MRU algorithm.

        If the number of items exceeds the maximum limit, the most recently used item
        will be discarded.

        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.

        """
        if key is None or item is None:
            return

        # Assign the item value to the key in cache_data
        self.cache_data[key] = item

        # Update the order of recently used items
        self.mru_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently used item from cache_data
            item_discarded = next(iter(self.mru_order))
            del self.cache_data[item_discarded]
            print(f"DISCARD: {item_discarded}")

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used item from mru_order
            self.mru_order.popitem(last=False)

        # Move the current key to the front of mru_order
        self.mru_order.move_to_end(key, last=False)

    def get(self, key):
        """Returns the value associated with the key in the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is None or doesn't exist in the cache.

        """
        if key is not None and key in self.cache_data:
            # Move the current key to the front of mru_order
            self.mru_order.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
