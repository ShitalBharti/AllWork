class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, val):
# Compare the new value with the parent node
      if self.data:
         if val < self.data:
            if self.left is None:
               self.left = Node(val)
            else:
               self.left.insert(val)
         elif val > self.data:
            if self.right is None:
               self.right = Node(val)
            else:
               self.right.insert(val)
      else:
         self.data = val

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data)
      if self.right:
         self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()