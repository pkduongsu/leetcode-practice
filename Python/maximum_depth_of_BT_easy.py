#BFS:
#Time: O(n) - worst case
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        q = deque()
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        return depth
    
#recursive DFS: Time: O(n) - worst case
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
#iterative DFS: Time (O(n))
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        depth = 0
        
        while stack:
            node, currentDepth = stack.pop()

            if node:
                depth = max(depth, currentDepth)
                stack.append([node.left, currentDepth + 1])
                stack.append([node.right, currentDepth + 1])

        return depth
