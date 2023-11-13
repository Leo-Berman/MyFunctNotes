def symmetrictree(root1,root2): 
    # default boolean      
    mybool = True
    
    # check to see if tree is empty
    if(root1 == None) & (root2 == None):
        return True
    
    # check to see if one side of the tree is null and the other isn't
    if(root1 == None) | (root2 == None):
        return False
    
    # check if values are the same, if so call the function for their brancehes
    if(root1.value == root2.value):
        if(symmetrictree(root1.left,root2.right)==False):
            return False
        if(symmetrictree(root1.right,root2.left)==False):
            return False
    
    # if they aren't the same return False
    else:
        return False
        
    # if no flags raised return True
    return True