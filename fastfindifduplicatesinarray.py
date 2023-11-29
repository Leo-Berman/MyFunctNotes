def solution(a):
    if (len(a) == 0) or (len(a) == 1):
        return False
    else:
        a.sort()
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                return True
        
        return False