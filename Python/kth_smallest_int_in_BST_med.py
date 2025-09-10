#Brute force: use arr.sort()
#Time O(n logn)
#Space: O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        stack = [root]
        arr = []

        while stack:
            node = stack.pop()
            arr.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        arr.sort()

        return arr[k - 1]
    
#Optimal: iteratively go through left (smaller values first), then right -> O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        n = 0 #number of visited elements
        current = root

        while stack or current: #stack can be empty due to the initial state -> use or
            while current:
                stack.append(current) #add the visited node
                current = current.left #and move the pointer to  the left node (with smaller values)

            #after all smaller values are added (current becomes null)
            current = stack.pop()
            n += 1
            if n == k:
                return current.val   
            current = current.right