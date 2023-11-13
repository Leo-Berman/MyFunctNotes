def solution(t1, t2):
    def issametree(root1,root2): 
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
            if(issametree(root1.left,root2.left)==False):
                return False
            if(issametree(root1.right,root2.right)==False):
                return False
        
        # if they aren't the same return False
        else:
            return False
            
        # if no flags raised return True
        return True
    
    def checkroots(root1,root2):
        # check to see if there are any more points to check
        if(root1 == None):
            return False
        
        # check to see if the current node has the same head as the head of the other tree
        if(root1.value == root2.value):
            #print("in loop")
            if issametree(root1,root2) == True:
                return True
        if (checkroots(root1.left,root2) | checkroots(root1.right,root2)) == True:
            return True
        return False
            
    if(t2 == None):
        return True        
    return(checkroots(t1,t2))
