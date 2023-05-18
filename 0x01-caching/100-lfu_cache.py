#!/usr/bin/python3
"""
LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that represents a caching system using LFU  algorithm

    Args:
        BaseCaching: The base caching class to inherit from.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.item_freqs = {}  # Tracks the frequency of cache items

    def put(self, key, item):
        """
        Gives the item value to the key in the cache using LFU algo.

        Args:
            key (hashable): The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is None or item is None:
            return

        # Assign the item value to the key in cache_data
		self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            # Find the key with the minimum frequency
			item_to_discard = min(self.item_freqs, key=self.item_freqs.get)
            self.item_freqs.pop(item_to_discard)
            self.cache_data.pop(item_to_discard)
            print(f"DISCARD: {item_to_discard}")

        if key not in self.item_freqs:
			# Initialize the frequency for a new item
			self.item_freqs[key] = 0
        else:
            # Increment the frequency of an existing item
			self.item_freqs[key] += 1

    def get(self, key):
        """Returns the value associated with the key in the cache.
        Args:
            key (hashable): The key of the item to retrieve.
        Returns:
            The value associated with the key, 
            or None if the key is None or doesn't exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.item_freqs[key] += 1  #Increment d frequency of accessed item

        return self.cache_data.get(key)
