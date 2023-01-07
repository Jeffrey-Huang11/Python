# Hashmap implementation with using seperate chaining (linked list) to address collisions
from linked_list import Node, LinkedList

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
  
  def hash(self, key):
    return sum(key.encode())
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value): 
    hashcode = self.hash(key)
    array_index = self.compress(hashcode)

    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for node in list_at_array:
      if node[0] == key:
        node[1] = value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    hashcode = self.hash(key)
    array_index = self.compress(hashcode)
    list_at_index = self.array[array_index]

    for node in list_at_index:
      if node[0] == key:
        return node[1]
    return None
