def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current: #guaranteed that we can execute till we find p, q, as they are guaranteed to be in tree
            if p.val > current.val and q.val > current.val:
                current = current.right #both are on right hand side, go down first node on left
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current