inputString = "foo(bar)baz"


def reverseInParentheses(inputString):
    for i in range(len(inputString)):
        if inputString[i] == "(":
            start = i
            #print (inputString[:start])
        if inputString[i] == ")":
            end = i
            #print (end)
            return reverseInParentheses(inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:])
    return inputString


print(reverseInParentheses("(bar)"))
