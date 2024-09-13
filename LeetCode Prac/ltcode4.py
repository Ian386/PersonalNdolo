def IsValidParantheses(str):
    stack = []
    close_to_open = {')': '(', '}': '{', ']': '['}
    for c in str:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


def remove_sorted_list_duplicates(nums):
    # use the concept of two pointers
    # l-pointer to keep track of the last element in the list where to insert the next unique element
    # r-pointer to iterate through the list to find the next unique element, compares itself with r-l and if not equal, then insert the element at l
    
    l=1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l]= nums[r]
            l+=1
    return l
    