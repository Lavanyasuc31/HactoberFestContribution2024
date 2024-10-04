import collections

class TimeMap:
    def __init__(self):
        # Initialize a dictionary to store the key-value pairs with timestamp
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key-value pair with a timestamp.
        :param key: Key to store.
        :param value: Value associated with the key.
        :param timestamp: The timestamp of the value.
        """
        # Append the (timestamp, value) tuple for the given key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieves the most recent value for the key at or before the given timestamp.
        :param key: Key to retrieve.
        :param timestamp: The maximum timestamp allowed.
        :return: Value associated with the key or None if no such value exists.
        """
        # If the key doesn't exist in the store, return None
        if key not in self.store:
            return None

        values = self.store[key]
        l, r = 0, len(values) - 1
        res = None

        # Perform binary search to find the largest timestamp <= given timestamp
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # Record the value if timestamp matches
                l = mid + 1
            else:
                r = mid - 1

        return res

# Test Cases
kv = TimeMap()

# Set key-value pairs
kv.set("foo", "bar", 1)   # Store 'foo' with value 'bar' at timestamp 1
print(kv.get("foo", 1))    # Output: "bar" (value found at timestamp 1)
print(kv.get("foo", 3))    # Output: "bar" (most recent value <= timestamp 3)
kv.set("foo", "bar2", 4)   # Update 'foo' with value 'bar2' at timestamp 4
print(kv.get("foo", 4))    # Output: "bar2" (value found at timestamp 4)
print(kv.get("foo", 5))    # Output: "bar2" (most recent value <= timestamp 5)
