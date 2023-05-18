from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class that represents a caching system using the LRU (Least Recently Used) algorithm"""

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """Assigns the item value to the key in the cache using the LRU algorithm.

        If the number of items exceeds the maximum limit, the least recently used item
        will be discarded.

        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_recently_used_key = self.key_order.pop(0)
                del self.cache_data[least_recently_used_key]
                print(f"DISCARD: {least_recently_used_key}")

            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

    def get(self, key):
        """Returns the value associated with the key in the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is None or doesn't exist in the cache.
        """
        if key is not None and key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None

