# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        linked_pair = LinkedPair(key, value) 
        hash_mod = self._hash_mod(key)
        current_pair = self.storage[hash_mod]
        while current_pair is not None and current_pair.key is not key: 
            last_pair = current_pair
            current_pair = last_pair.next
        if current_pair is None: 
            linked_pair.next = self.storage[hash_mod]
            self.storage[hash_mod] = linked_pair
        else: 
            current_pair.value = value     




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_mod = self._hash_mod(key)
        current_pair = self.storage[hash_mod]
        if current_pair is not None and current_pair.next is None: 
            self.storage[hash_mod] = None
        elif current_pair is not None and current_pair.next is not None: 
            last_pair = current_pair.next 
            self.storage[hash_mod] = last_pair
        else: 
            print('Key was not found')
    
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_mod = self._hash_mod(key)
        current_key = key 
        current_pair = self.storage[hash_mod]
        if current_pair is None:
            return None
        while current_pair.key is not current_key: 
            last_pair = current_pair
            current_pair = last_pair.next 
        if current_key is current_pair.key: 
            return current_pair.value
        




    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2 
        




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")



