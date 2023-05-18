#!/usr/bin/python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class that represents a caching system using the LIFO algo"""

    def __init__(self):
        """Initialize the LIFOCache"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using the LIFO algo
        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    last_item = self.key_indexes.pop()
                    # Remove the last item - LIFO
                    del self.cache_data[last_item]
                    print("DISCARD:", last_item)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """Returns the value associated with the key in the cache.
        Args:
            key: The key to retrieve the value for.
        Returns:
            The value associated with the key,
            or None if the key is None or doesn't exist in the cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
