# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#input: root node of a binary tree: root: Optional[treeNode]

#output: list of values of nodes that are visible from the right side of the tree, ordered by top to bottom
#- > list[int]

#Optional: can be none
#def RightSideView(self, root: Optional[TreeNode]) -> List[int]

#I'd say, track if it has right nodes? if not, add to the result array

#Assuming Valid BST: greater values on the right, smaller on left
#can we reframe the problem to: largest value of each level?
#no, we should aim to just iterate through the vals on the right hand side first
#and since we're using DFS, first time we visit that right node is the right most node
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [[root, 0]]  # (node, depth)

        while stack:
            node, depth = stack.pop()
            if node is None:
                continue

            # first time we reach this depth (since we go right-first)
            if depth == len(res):
                res.append(node.val)

            # push left first, then right so right is processed first (LIFO)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

        return res

#Time: O(n), Space: O(n) - n is number of nodes in tree

#if we're using BFS then, track the values on the right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root]) #Queue: LIFO - last in first out
        res = []

        while q:
            rightNode = None
            #get the current level length before starting the loop
            #lets iterate:
            #root: currentLevelLen = 1
            #in 1 iteration of the for loop:
            #pop root:
            #right node = root
            #end loop
            #rightNode of first level = root

            #iter 2:
            #2nd level - root left, right => len = 2 => 2 iterations in for loop -> only pop the 2 nodes in queue (2 level 2 nodes)
            #in 1st iter of the for loop
            #rightNode = root.left
            #add 2 left, right of that root.left
            #iter2 in the for loop: rightNode = root.right
            #add 2 left, right of that root.left

            #=> with the adequate number of iterations, we can go through all nodes from left to right
            #of a level, and the final node will be the right most
            
            #same for last iter, levelLength = 4
            #-> pop 4 elements in the queue, last being the rightmost node
            #=> by the end of for loop, we get the rightmost node, while there are just no next values
            


            currentLevelLen = len(q)
            
            #be careful to only add left, right nodes if they are available, as adding None can extend the queue length
            #unnecessarily, and cause infinite loops

            for i in range(currentLevelLen):
                current = q.popleft()
                if current:
                    rightNode = current
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)

            if rightNode:
                res.append(rightNode.val)

        return res
#Time: O(n) Space: O(n) - n is number of nodes in tree