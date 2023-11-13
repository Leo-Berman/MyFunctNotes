# function for printing an entire tree from the head down
def displaytree(head):
    
    if head.left == None:
        return None
    
    print(head.left.profession)
    print(head.right.profession)
    displaytree(head.left)
    displaytree(head.right)