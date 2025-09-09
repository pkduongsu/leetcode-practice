def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current: #guaranteed that we can execute till we find p, q, as they are guaranteed to be in tree
            if p.val > current.val and q.val > current.val:
                current = current.right #both are on right hand side, go down first node on left
            elif p.val < current.val and q.val < current.val:
                current = current.left #both are on left hand side, go down first node on left
            else: #when one is root, (p.val == current.val or q.val == current.val) we can just return root as it will always be the lowest ancestor possible
                #or when theres a split, p.val < current.val and q.val > current.val -> lowest ancestor is the split point, we can just return it now.      
                return current