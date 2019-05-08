from nodes import nodes

# print(nodes)

def number(node):
  if not node:
    return 0
  
  left = number(node.left)
  right = number(node.right)
  
  return left + right + 1

print("number: " + str(number(nodes[1])))
