#DFS: # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#how do we define a tree node?
#Given that we're examining a BST:
# node: value, left, right pointers

#class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

#Input: root node of a BST
#output: the number of good nodes within the tree -> int
#def GoodNodes(self, root: TreeNode) -> int:

#good node: the path from root of the tree to node x contains no nodes with a value greater than 
#value of node x

#does this include tha value of the root node?

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        s = [[root, float("-inf")]]

        while s:
            current, maxVal = s.pop()
            #this solution using the prev pointer is not feasible, as how can we even get the
            #previous pointer of the previous node when we switch current  to prev.

            #instead, track the maxval in the path
            #so the root node is by default a good node, as theres no value greater than itself before it

            #counting the greater values also takes into account of the root node

            #ex: 3 -> 1 - > 2 => 1 is not a good node (root 2 > 1), but 3 is (3 > 1, 3 > 2)
            if current.val >= maxVal:
                res += 1

            maxVal = max(maxVal, current.val)


            if current.right:
                s.append([current.right, maxVal])
            if current.left:
                s.append([current.left, maxVal])
            
        return res

#Time: O(n) where n is the number of nodes in the tree
#Space: O(n) - n is number of nodes in tree (stored in stack)

#BFS Same, just switch to queue:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#how do we define a tree node?
#Given that we're examining a BST:
# node: value, left, right pointers

#class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

#Input: root node of a BST
#output: the number of good nodes within the tree -> int
#def GoodNodes(self, root: TreeNode) -> int:

#good node: the path from root of the tree to node x contains no nodes with a value greater than 
#value of node x

#does this include tha value of the root node?

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        q = deque([[root, float("-inf")]])

        while q:
            current, maxVal = q.popleft()
            #this solution using the prev pointer is not feasible, as how can we even get the
            #previous pointer of the previous node when we switch current  to prev.

            #instead, track the maxval in the path
            #so the root node is by default a good node, as theres no value greater than itself before it

            #counting the greater values also takes into account of the root node

            #ex: 3 -> 1 - > 2 => 1 is not a good node (root 2 > 1), but 3 is (3 > 1, 3 > 2)
            if current.val >= maxVal:
                res += 1

            maxVal = max(maxVal, current.val)


            if current.left:
                q.append([current.left, maxVal])
            if current.right:
                q.append([current.right, maxVal])
            
        return res
        
        
#recursive approach:

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
        
