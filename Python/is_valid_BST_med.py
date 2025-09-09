# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS solution: recursively evaluate boundaries of the current node.
#Time: O(n)
#Space: O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #left boundary and right boundary: condition for the current node
        def isValidNode(node: TreeNode, left, right) -> bool:
            if not node: #for any recursive, hit null -> return 
                return True

            if not (node.val < right and node.val > left):
                return False

            return (isValidNode(node.left, left, node.val) 
            and isValidNode(node.right, node.val, right))

        return isValidNode(root, float("-inf"), float("inf"))
    
#BFS -> FIFO -> queue    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        #make a queue where elements include current node, left, and right boundaries
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val)) #add the left node, current left, and the current parent node value as right boundary -> check if its smaller than the current parent node value
            if node.right:
                q.append((node.right, node.val, right))#add the right node, the current parent node value as left boundary -> check if its larger than the current parent node value

        return True
        
    

