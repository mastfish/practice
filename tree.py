class Node(object):
  __slots__= "left", "right", "value",

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def insert(tree, value):
  if (tree == None):
    return Node(value)
  if (tree.value < value):
    tree.left = insert(tree.left, value)
  else:
    tree.right = insert(tree.right, value)
  return tree

n1 = Node(7)
n2 = Node(2)
n8 = Node(8)

tree = Node(0)
insert(tree, 7)
insert(tree, 8)
insert(tree, 9)
insert(tree, -1)

print tree.left.value
print tree.left.left.left.value
print tree.right

