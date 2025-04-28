## Section 3: Trees
# 5. Lowest Common Ancestor (LCA) of a Binary Tree:**
#  Given a binary tree and two nodes, find their Lowest Common Ancestor.
#  Implement a recursive solution.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LCA(root, n1, n2):
    # Base case: if root is None or root is one of the nodes
    if root is None or root.data == n1 or root.data == n2:
        return root
    
    # Recursively find LCA in the left and right subtrees
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)

    # If both left and right are non-None, then root is LCA
    if left and right:
        return root
    
    # Otherwise, return the non-None child
    return left if left else right

# Example 
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
# Find LCA of nodes 5 and 1
lca = LCA(root, 5, 1)
print("LCA of 5 and 1: " ,lca.data)


# 6. Serialize and Deserialize a Binary Tree:
# Design an algorithm to serialize and deserialize a binary tree.
# Ensure the solution efficiently encodes and decodes the structure of the tree


        

