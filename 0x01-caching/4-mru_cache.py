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
        self.most_ru_order = OrderedDict()

    def put(self, key, item):
        """Gives the item value to the key in the cache using the MRU algo
        If the number of items exceeds the maximum limit,
        the most recently used item will be discarded.

        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is None or item is None:
            return

        # Assign the item value to the key in cache_data
        self.cache_data[key] = item

        # Update the order of recently used items
        self.most_ru_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently used item from cache_data
            most_recently_item = next(iter(self.most_ru_order))
            del self.cache_data[most_recently_item]
            print(f"DISCARD: {most_recently_item}")

        if len(self.most_ru_order) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used item from MRU order
            self.most_ru_order.popitem(last=False)

        # Move the current key to the front of most recently used order
        self.most_ru_order.move_to_end(key, last=False)

    def get(self, key):
        """Returns the value associated with the key in the cache.
        Args:
            key: The key to retrieve the value for.
        Returns:
            The value associated with the key,
            or None if the key is None / doesn't exist in the cache
        """
        if key is not None and key in self.cache_data:
            # Move the current key to the front of MRU order
            self.most_ru_order.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
