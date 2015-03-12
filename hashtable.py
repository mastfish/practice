class Hash:

  def __init__(self):
    self.array = [None] * 50
    
  def insert(self, key, value):
    self.array[key:(key+2)] = value

  def find(self, key):
    self.array[key]

  def delete(self, key):
    self.array[key] = None

hash = Hash()
print len(hash.array)

hash.insert(5, 'g')

print hash.find(5)

hash.delete(5)

print hash.find(5)

print hash

print hash.array[5]

print hash.array

print len(hash.array)