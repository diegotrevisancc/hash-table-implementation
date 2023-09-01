class AgendaHeroes:
  def __init__(self):
    self.size = 26
    self.table = [None] * self.size
    self.totalItems = 0

  def hash_function(self, key):
    indexFirstChar = int(((ord(key[0].lower()) / 98) - 1) * 100) + 1
    # print("index: {} - value: {}".format(indexFirstChar, key))
    return indexFirstChar

  def insert(self, key):
    index = self.hash_function(key)
    if self.table[index] is None:
      self.table[index] = key
    else:
      if type(self.table[index]) != list:
        existingItem = self.table[index]
        self.table[index] = [existingItem, key]
      else:
        array: list = self.table[index]   
        array.append(key)
        array.sort()
    
    self.totalItems += 1
    return True

  def search(self, key):
    index = self.hash_function(key)
    if self.table[index] == key:
      return self.table[index]
    if type(self.table[index]) == list:
      return self.__findInColision(key, index)
    return None
  
  def __findInColision(self, key, index):
    array = self.table[index]
    for item in array:
      if item == key:
        return key
    return None


hash_table = AgendaHeroes()
hash_table.insert("aa")
hash_table.insert("b")
hash_table.insert("z")
hash_table.insert("z2")
hash_table.insert("zzzz")
hash_table.insert("z1")
print(hash_table.table)

print(hash_table.search("aa"))
print(hash_table.search("b"))
print(hash_table.search("z"))
print(hash_table.search("z2"))
print(hash_table.search("eu nao existo"))