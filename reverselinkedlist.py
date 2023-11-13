def reverselist(head):
    # check for lists shorter than 3
    if head == None:
        return None
    if head.next == None:
        return head
    if head.next.next == None:
        ptr1 = head
        ptr2 = head.next
        ptr1.next = None
        ptr2.next = ptr1
        return ptr2
    
    # set the pointers
    P1 = head
    P2 = head.next
    P3 = P2.next
    
    # do the first round
    P1.next = None
    P2.next = P1
    
    while(P3):
        P1 = P2
        P2 = P3
        P3 = P3.next
        P2.next = P1
    
    return P2