#28. Find the Index of the First Occurrence in a String


#Solution1
def find_first_occurrence(haystack, needle):
    if needle == "":
        return 0
    
    for h in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if haystack[h+j] != needle[j]:
                break
            if j == len(needle) - 1:
                return h
    return -1



#Solution2
def find_first_occurrence(haystack, needle):
    if needle == "":
        return 0
    
    for h in range(len(haystack) + 1 - len(needle)):
        if haystack[h:h + len(needle)] == needle:
            return h
    return -1