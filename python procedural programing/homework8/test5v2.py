def r_palindrome(string):
    if len(string) <= 2 and string[0] == string[-1]:
        return True
    if string[0] != string[-1]:
        return False
    return r_palindrome(string[1:-1:])


print(r_palindrome("asddsa"))
print(r_palindrome("abcddcba"))
print(r_palindrome("as"))