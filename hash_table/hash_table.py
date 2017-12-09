from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def index_of_bucket(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """
        Return a list of all keys in this hash table.
        Running time: O(n^2)
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)

        return all_keys

    def values(self):
        """
        Return a list of all values in this hash table.
        Running time: O(n) 
        """

        bucket_items = self.items()

        # Iterate through all key, value pairs and only grab the value
        bucket_values = [ item[1] for item in bucket_items ]

        return bucket_values 
             
        

    def items(self):
        """
        Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n)
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """
        Return the number of key-value entries by traversing its buckets.
        Running time: O(n)
        """
        buckets_length = 0
        for bucket in self.buckets:
            buckets_length += len(bucket.items())

        return buckets_length


    def contains(self, key):
        """
        Return True if this hash table contains the given key, or False.
        Running time: O(n)
        """
        bucket_index = self.index_of_bucket(key)
        bucket = self.buckets[bucket_index]
        bucket_items = bucket.items()

        for item in bucket_items:
            if key in item:
                return True
        
        return False

    def get(self, key):
        """
        Return the value associated with the given key, or raise KeyError.
        Running time: O(n)
        """
        bucket_index = self.index_of_bucket(key)
        bucket = self.buckets[bucket_index]
        if bucket.is_empty():

            raise KeyError('Key not found: {}'.format(key))
        
        bucket_items = bucket.items()
        for item in bucket_items:
            if key in item:
                return item[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """
        Insert or update the given key with its associated value.
        Running time: O(n)
        """
        bucket_index = self.index_of_bucket(key)
        bucket = self.buckets[bucket_index]

        if bucket.is_empty():
            bucket.prepend((key, value))
        else:
            key_exist = self.contains(key)
            if key_exist:
                old_value = self.get(key)
                bucket.delete((key, old_value))
                bucket.prepend((key, value))
            else:
                bucket.prepend((key, value))

    def delete(self, key):
        """
        Delete the given key from this hash table, or raise KeyError.
        Running time: O(n)
        """
        bucket_index = self.index_of_bucket(key)
        bucket = self.buckets[bucket_index]
        bucket_value = self.get(key)
        bucket.delete((key, bucket_value))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()