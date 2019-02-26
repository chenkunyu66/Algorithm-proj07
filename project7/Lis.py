#cse 331
#chen,kunyu
#This project is to implement a dynamic program that
#solves the longest increasing subsequence problem.

def verify_subseq(seq, subseq):
    """Determines whether one list is a subsequence of another."""
    h1 = 0
    for x in subseq:
        #check x in the seq or not
        while h1 < len(seq) and seq[h1] != x:
            h1 += 1
        #if x in the seq, h1 still +=1 
        if h1 < len(seq):
            h1 += 1
        else:
            return False
    return True


def verify_increasing(seq):
    """Determines whether a list is in increasing order."""
    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:
            return False
    return True


def find_lis(seq):
    """Finds the longest increasing subsequence of the given list."""
    
    a, pre, last = [], [None] * len(seq), -1
    #check each item in the seq 
    for i in range(len(seq)):
        x = seq[i]
        #if list a is none or x large than the found item in the seq
        if len(a) == 0 or x > seq[a[-1]]:
            #if a is not empty 
            if len(a) > 0:
                pre[i] = a[-1]
            a.append(i)
            last = i
        else:
            #using binary search to find the closest number of x
            #mid is the closest number
            #if x is larger than the number we find,then the closest \n
            #number is in the high part
            #otherwise, the closest number is in the low part
            low, high = 0, len(a) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if seq[a[mid]] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            a[low] = i
            if low > 0:
                pre[i] = a[low - 1]
    ans = []
    while last is not None:
        ans.append(seq[last])
        last = pre[last]
    return ans[::-1]

