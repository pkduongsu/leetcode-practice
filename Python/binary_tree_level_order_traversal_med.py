#BFS: 
from collections import deque
from typing import Optional, List
# time complexity O(n), memory: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)
        
        while queue:
            currentLevel = []

            for i in range(len(queue)):
                node = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(currentLevel)

        return res
    
#can you implement solution with DFS?
#Time: O(n) Space: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #try to implement with DFS?
        if not root:
            return []

        stack = [[root, 0]]
        res = []

        while stack:
            node, depth = stack.pop()
            if not node:
                continue
            #for the result array, each depth is the index of the element (sub array that contains child nodes in that depth)
            if len(res) == depth:
                res.append([])
                    
            #critical, as this allow adding value to the correct depth subarray, even though further depth will be processed first in the queue 
            res[depth].append(node.val)

            #push right first so left (last in) is processed first
            stack.append([node.right, 1 + depth])
            stack.append([node.left, 1 + depth])
        
        return res
                