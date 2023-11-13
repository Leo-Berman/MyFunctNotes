# write a function to merge list
def mergelist(list1,list2):
    # return list
    ret = list1
    
    # iterate to last element of list1
    while(list1.next!=None):
        list1 = list1.next
    
    print(list1.value)
    # link the lists
    list1.next = list2
    
    return ret