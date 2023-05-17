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
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the last inserted key (LIFO)
                self.discard = self.last_inserted_key()
                self.cache_data.pop(self.discard)
                print('DISCARD:', self.discard)

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

    def last_inserted_key(self):
        """Returns the last inserted key in the cache.

        Returns:
            The last inserted key,
            or None if the cache is empty.
        """
        if self.cache_data:
            return list(self.cache_data.keys())[-1]
        return None
