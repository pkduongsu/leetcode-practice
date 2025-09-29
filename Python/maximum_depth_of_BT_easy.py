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
    
#given root, return maximum depth
#we think of traversing through the tree and memorize the current depth of node somehow
#-> stack element will be the node, along with its depth (init by root, 1)
#if we append the node on lower depth (left, right), append with the prev node depth + 1
#update a global value for memorizing max depth
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 1]])

        if not root:
            return 0

        maxDepth = 0
        while q:
            currentNode, currentDepth = q.popleft()

            maxDepth = max(maxDepth, currentDepth)

            if currentNode.left:
                q.append([currentNode.left, currentDepth + 1])
            if currentNode.right:
                q.append([currentNode.right, currentDepth + 1])

        return maxDepth

#! BIG O space complexity measures maximum memory used at any moment during the run (peak/working set), not what remains in the end.

#recursive DFS: Time: O(n) - worst case
#Space:
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
