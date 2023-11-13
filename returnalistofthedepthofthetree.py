# find function by depth
def finddepth(head,depth,mylist):
    if(depth == 1):
        mylist.append(head.left)
        mylist.append(head.right)
        return None
    finddepth(head.left,depth-1,mylist)
    finddepth(head.right,depth-1,mylist)