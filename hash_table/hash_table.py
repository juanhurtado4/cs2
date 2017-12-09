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
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n^2) Why and under what conditions?"""
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
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        # TODO: Call items()
        # TODO: Count items

        buckets_length = 0
        for bucket in self.buckets:
            buckets_length += len(bucket.items())

        return buckets_length


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?: 
        Answer: O(n) Because finding bucket index is constant time and then iterate through that bucket which is O(n). In addition, we save time because we can find the location using bucket_index func"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        bucket_index = self.index_of_bucket(key)
        bucket = self.buckets[bucket_index]
        bucket_items = bucket.items()

        for item in bucket_items:
            if key in item:
                return True
        
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs O(1)
        # TODO: Check if key-value entry exists in bucket O(n)
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self.index_of_bucket(key)
        bucket = self.buckets[bucket_index]
        if bucket.is_empty():
            # import pdb; pdb.set_trace()
            raise KeyError('Key not found: {}'.format(key))
        
        bucket_items = bucket.items()
        for item in bucket_items:
            if key in item:
                return item[1]

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs O(1)
        # TODO: Check if key-value entry exists in bucket O(n)
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket_index = self.index_of_bucket(key)
        bucket = self.buckets[bucket_index]
        if bucket.is_empty:
            bucket.prepend((key, value))
        else:
            bucket_data = bucket.find((key, value))
            if bucket_data == None:
                bucket.prepend((key, value))
            else:
                bucket.delete((key, value))
                bucket.prepend((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
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

    # Enable this after implementing delete method
    delete_implemented = False
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
