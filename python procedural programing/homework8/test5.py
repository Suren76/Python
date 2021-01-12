# def palindrome(string):
#    if string == string[::-1]:
#        return True
#    else:
#        return False


# print(palindrome("asddsa"))
# print(palindrome("abcddcba"))


def r_palindrome(string):

    if len(string) <= 2:
        return True
    if string[0] != string[-1]:
        return False
    return r_palindrome(string[1:-1:])


print(r_palindrome("asddsa"))
print(r_palindrome("abcddcba"))
