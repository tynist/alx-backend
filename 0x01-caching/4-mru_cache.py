#!/usr/bin/python3
"""
MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class that represents a caching system using the MRU (Most Recently Used).
    Inherits from the BaseCaching class.
    """

    def __init__(self):
        """Initialize the MRUCache."""
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using the MRU alg
        If the number of items exceeds the maximum limit,
        the most recently used item will be discarded.

        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                most_recently_used_key = next(reversed(self.cache_data))
                del self.cache_data[most_recently_used_key]
                print(f"DISCARD: {most_recently_used_key}")

    def get(self, key):
        """
        Returns the value associated with the key in the cache.
        If the key is found, it promotes the key to the most
        recently used position.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is None or doesn't exist in the cache.
        """
        if key is not None and key in self.cache_data:
            # Promote the key to the most recently used position
            item = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = item
            return item
        return None
