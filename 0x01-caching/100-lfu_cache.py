#!/usr/bin/python3
"""
LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that represents a caching system using LFU (Least Frequently Used) algorithm.

    Args:
        BaseCaching: The base caching class to inherit from.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.item_frequencies = {}  # Tracks the frequency of cache items

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (hashable): The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            item_to_discard = min(self.item_frequencies, key=self.item_frequencies.get)
            self.item_frequencies.pop(item_to_discard)
            self.cache_data.pop(item_to_discard)
            print(f"DISCARD: {item_to_discard}")

        if key not in self.item_frequencies:
            self.item_frequencies[key] = 0  # Initialize the frequency for a new item
        else:
            self.item_frequencies[key] += 1  # Increment the frequency of an existing item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (hashable): The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key is None or doesn't exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.item_frequencies[key] += 1  # Increment the frequency of the accessed item
        return self.cache_data.get(key)
