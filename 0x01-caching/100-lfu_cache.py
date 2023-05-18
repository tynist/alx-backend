#!/usr/bin/python3
"""
LFU Caching
"""
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that represents a caching system using d LFU algo"""

    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.freqs = defaultdict(int)
        self.least_freq = float('inf')

    def put(self, key, item):
        """Gives the item value to the key in the cache using LFU algo.

        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is None or item is None:
            return

        # Assign the item value to the key in cache_data
        self.cache_data[key] = item

        # Update the frequency of the key
        self.freqs[key] += 1

        # Update the least frequency
        self.least_freq = min(self.least_freq, self.freqs[key])

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            itms_to_discard = [p for p, q in self.freqs.items() if q == self.least_freq]

            if len(itms_to_discard) > 1:
                # Use LRU algorithm to discard the LRU item(s)
                least_ru_item = min(itms_to_discard, key=lambda p: self.timestamps[p])
                itms_to_discard.remove(least_ru_item)

            for item in itms_to_discard:
                del self.cache_data[item]
                del self.freqs[item]
                print(f"DISCARD: {item}")

            self.least_freq += 1

        # Update the timestamp of the key
        self.timestamps[key] = self.current_time
        self.current_time += 1

    def get(self, key):
        """Returns the value associated with the key in the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is None or doesn't exist in the cache.

        """
        if key is not None and key in self.cache_data:
            # Update the frequency and timestamp of the key
            self.freqs[key] += 1
            self.timestamps[key] = self.current_time
            self.current_time += 1
            return self.cache_data[key]
        return None
