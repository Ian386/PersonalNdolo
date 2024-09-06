# Palindrome number
# Without converting the number to string
# 121 -> True
# -121 -> False
def Palindrom_Num(num):
    if num < 0: return False
    temp = num
    rev = 0
    while temp:
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return rev == num


def IsPalindrome(x):
    if x < 0: return False
    div =1
    while x >= 10 * div: div *= 10
    while x:
        l = x // div
        r = x % 10
        if l != r: return False
        x = (x % div) // 10
        div //= 100
    return True


""" Efficiency Comparison
Time Complexity: Both functions have the same time complexity of O(log10(n)).
Space Complexity: Both functions use constant space, i.e., O(1).
Key Differences:
Palindrom_Num explicitly reverses the number and then checks equality, while IsPalindrome directly compares corresponding digits from the start and end. This makes IsPalindrome slightly more efficient in practice for large numbers since it may exit early if a mismatch is found (without fully reversing the number).
If the palindrome check fails early in IsPalindrome, it might outperform Palindrom_Num, which always completes the entire reverse operation.
Both are efficient, but IsPalindrome might have a slight edge due to potential early termination. """