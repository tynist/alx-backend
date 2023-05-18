#!/usr/bin/python3
"""
LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class that represents a caching system using the LRU algorithm"""

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.key_order = []  # List to manage the order of key access

    def put(self, key, item):
        """Gives the item value to the key in the cache using the LRU algo
        If the number of items exceeds the maximum limit,
        the least recently used item (least_used_key) will be discarded.

        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used_key = self.key_order.pop(0)
                del self.cache_data[least_used_key]
                print(f"DISCARD: {least_used_key}")

            # Update the key's order to reflect its most recent use
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

    def get(self, key):
        """Returns the value associated with the key in the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is None / doesn't exist in the cache
        """
        if key is not None and key in self.cache_data:
            # Update the key's order to reflect its most recent use
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None
