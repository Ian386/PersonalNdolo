#LeetCode 1
def SumTwoNums(list, target):
    HashMapPrev = {} # store in value: index
    for i, n in enumerate(list):
        rem = target -n
        if rem in HashMapPrev:
            return [HashMapPrev[rem], i]
        HashMapPrev[n] = i
    return

print(SumTwoNums([2,7,11,15], 9)) # [0,1]