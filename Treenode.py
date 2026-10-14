class Treenode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None
#function
def insert(root, key):
    if root is None: # base case
        return Treenode(key)
    
    if key < root.val: # recursive case
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
root = Treenode(10)
insert(root, 5)
insert(root, 15)
insert(root, 7)
insert(root, 12)
insert(root, 18)

insert(root, 6)


