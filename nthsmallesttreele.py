def solution(t, k):

    def nthleast(t,k,count,ans):
        #check if you've reached the end of the list    
        if(t == None):
            return

        # solve the left branch
        nthleast(t.left,k,count,ans)
        
        # check to see if this node is the node
        count[0]+=1
        #print("t = ",t.value,"count = ",count)
        if count[0] == k:
            #print("FoUND!")
            ans[0] = t.value
            return
            
        # if not check to the right of thnode
        nthleast(t.right,k,count,ans)

    myans = [0]
    mycount = [0]
    nthleast(t,k,mycount,myans)
    
    return myans[0]
    
