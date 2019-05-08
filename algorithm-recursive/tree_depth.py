from nodes import nodes

# print(nodes)

def depth(node):
  if not node:
    return 0
  
  left = depth(node.left)
  right = depth(node.right)
  
  return max(left, right) + 1

print("depth: " + str(depth(nodes[1])))
