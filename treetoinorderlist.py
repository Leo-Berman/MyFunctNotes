#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    def inorder(mylist,worklist):
        if len(worklist) == 0:
            return
        worklist2=[]
        for ele in worklist:
            if ele.left != None:
                mylist.append(ele.left.value)
                worklist2.append(ele.left)
            if ele.right != None:
                mylist.append(ele.right.value)
                worklist2.append(ele.right)
        inorder(mylist,worklist2)
    if t == None:
        return []
    retlist = []
    retlist.append(t.value)
    firstworklist = []
    firstworklist.append(t)
    inorder(retlist,firstworklist)
    return retlist