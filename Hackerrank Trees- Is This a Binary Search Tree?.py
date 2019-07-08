""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
a = []

def checkBST(root):
    last = -1
    path = []
    while path or root :
        if root :
            path.append(root)
            root = root.left
        else:
            root = path.pop()
            if last >= root.data:
                return False
            last = root.data
            root = root.right

    return True

    #node = root
    #nodeLeft = root.left
    #nodeRight = root.right
    #if nodeLeft.data < node.data:
    #    checkBST(node.left)
    #if nodeRight.data > node.data:
    #    checkBST(node.right)
    #print(Yes)
