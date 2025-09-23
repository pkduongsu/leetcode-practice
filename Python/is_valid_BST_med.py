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

            if not (node.val < right and node.val > left): #if the value is not in the defined range, return False
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
        
        
#Iterative DFS:
#Time complexity: O(n) where n is the maximum length of the tree (number of nodes)
#Space complexity: O(n) where n is also the number of nodes in the tree (storing array of nodes, left, right)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       #first question to ask is: is there any upper/lower boundaries for a node's value?
       # if they answer, ex: not infinite, but [-1000, 1000]:
       # go ahead and explain the boundary approach
       # Root node: Boundary: [-1000, 1000], Value: node.val
       # Left node: Boundary: [-1000, node.val], Value: node.left -> needs to check it against the boundaries, false -> return false (not valid BST)
       # Same for the right node: [node.val, 1000], Value: node.right -> if false, return false
       # With this logic, we now only need to implement it with a traversal algo: BFS, DFS, Iterative DFS

       #BFS: Queue (LIFO)
       #Iterative DFS: Stack (FIFO)
        s = [[root, -1000, 1000]]
    
        def isValidNode(node: TreeNode, left, right) -> bool:
            if (node.val > left and node.val < right):
                return True
            else: return False

        if not root:
            return True
        
        while s:
            current, left, right = s.pop()

            if not isValidNode(current, left, right):
                return False
            
            if current.left:
                s.append([current.left, left, current.val])

            if current.right:
                s.append([current.right, current.val, right])

        return True
            



        

        
    

