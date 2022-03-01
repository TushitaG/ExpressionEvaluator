
# Hashtable to store the expressions and answers for the math game
class HashTable:
    def __init__(self,size,expList):
        self.size = size
        self.expList = expList
        self.keys = [None] * self.size
        self.buckets = [None] * self.size

    # A simple remainder method to convert key to index
    def hashFunction(self, key ):
        return self.expList.index(key)
    
    # Deal with collision resolution by means of
    # linear probing with a 'plus 1' rehash
    def rehashFunction(self, oldHash ):
        return (oldHash + 1) % self.size

    # Override the [] write item operator
    def __setitem__(self, key, value):
        index = self.hashFunction( key)
        startIndex = index
        while True:
            # If bucket is empty then just use it
            if self.buckets[index] == None:
                self.buckets[index] = value
                self.keys[index] = key
                break
            else: # If not empty and the same key then just overwrite
                if self.keys[index] == key:
                    self.buckets[index] = value
                    break
                else: # Look for another available bucket
                    index = self.rehashFunction(index)
                    # We must stop if no more buckets
                    if index == startIndex:
                        break

    def __getitem__(self,key):
        index = self.hashFunction(key)
        startIndex = index
        while True:
            if self.keys [index] == key: # Will be mostly the case unless value
                                         # had been previously rehashed at insertion
                                         # time
                return self.buckets[index]
            else: # Value for the key is somewhere else
                  # (due to imperfect hash function)
                index = self.rehashFunction(index )
                if index == startIndex:
                    return None