#BFS, time O(n), Space O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left #invert nodes

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

        
#DFS iterative: time O(n), space O(n)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]

        while stack:
            node = stack.pop()
            #in this loop, go through every possible values in tree and just invert left to right, right to left
            node.left, node.right = node.right, node.left #invert nodes

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
#DFS recursion: time O(n), space O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root