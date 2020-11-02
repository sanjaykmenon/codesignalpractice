'''
Given the string, check if it is a palindrome.

Example

    For inputString = "aabaa", the output should be
    checkPalindrome(inputString) = true;
    For inputString = "abac", the output should be
    checkPalindrome(inputString) = false;
    For inputString = "a", the output should be
    checkPalindrome(inputString) = true.
'''
def checkPalindrome(inputString):
    center = len(inputString)//2
    if len(inputString) % 2 == 1:
        if inputString[:center] == inputString[:center:-1]: #splitting the string.
            return True
        else:
            return False
    else:
        if inputString[:center] == inputString[:center-1:-1]:
            return True
        else:
            return False
# test commit