# write a function to merge list
def sortmergelist(list1,list2):
    # check if either list is empty if so return the other
    if list1 == None:
        return list2
    if list2 == None:
        return list1

    # check which list to make the head of your return
    if(list1.value < list2.value):
        ret = list1
        list1 = list1.next

        # if this empties the list link with the other list and return the whole thing
        if list1 == None:
            ret.next = list2
            return ret
    else:
        ret = list2
        list2 = list2.next
        if list2 == None:
            ret.next = list1
            return ret
    
    # loop through lists 
    tmp = ret    
    while(list1 and list2):

        # check which value is greater and link that value
        if (list1.value<list2.value):
            tmp.next = list1
            tmp = tmp.next
            list1 = list1.next
        else:
            tmp.next = list2
            tmp = tmp.next
            list2 = list2.next
        
        # check to see if list is emptied and if so link the other list
        if(list1 == None):
            tmp.next = list2
        if(list2 == None):
            tmp.next = list1
    
    # return the list
    return ret