def BT(self,root):
    if root:
        root.left, root.right = self.BT(root.right), self.BT(root.left)
    return root