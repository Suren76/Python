# For inputString = "aabaa", the output should be
# checkPalindrome(inputString) = true;
# For inputString = "abac", the output should be
# checkPalindrome(inputString) = false;
# For inputString = "a", the output should be
# checkPalindrome(inputString) = true.

def checkPalindrome(inputString):

    if type(inputString) == str and inputString.strip() == inputString and \
            1 <= len(inputString) <= 10**5:

        if(inputString == inputString[::-1]):
            return True
        else:
            return False

    else:
        return "You input incorrect data"


print(checkPalindrome("aabaa"))
print(checkPalindrome("abac"))
print(checkPalindrome("a"))
print(checkPalindrome(5))
