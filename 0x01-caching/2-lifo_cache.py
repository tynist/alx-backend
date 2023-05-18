"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class that represents a caching system using the LIFO algo"""

    def __init__(self):
        """Initialize the LIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Assigns d item value to d key in the cache using d LIFO algo
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
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)
            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """Returns the value associated with the key in the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is None / doesn't exist in the cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
