class Node:
  def __init__(self,x):
    self.left = None
    self.right = None
    self.val = x

nodes = []

for i in range(12):
  nodes.append(Node(i))

nodes[1].left = nodes[2]
nodes[1].right = nodes[3]

nodes[2].left = nodes[4]
nodes[2].right = nodes[5]

nodes[3].left = nodes[6]
nodes[3].right = nodes[7]

nodes[4].left = nodes[8]
nodes[4].right = nodes[9]

nodes[7].left = nodes[10]

nodes[9].right = nodes[11]

"""
for node in nodes:
  print('node: ' + str(node.val))
  if node.left:
    print('left: ' + str(node.left.val))
  if node.right:
    print('right: ' + str(node.right.val))
"""
