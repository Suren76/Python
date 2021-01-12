# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

inputArray = ["aba", "aa", "ad", "vcd", "aba"], [
    "asis", "fg", "sos", "aa", "ad"]


def allLongestStrings(inputArray):

    len_word = 0

    for word in inputArray:
        if len(word) > len_word:
            len_word = len(word)

    longest_str = []

    for word in inputArray:
        if len(word) == len_word:
            longest_str.append(word)

    return longest_str


print(allLongestStrings(inputArray[0]))
print(allLongestStrings(inputArray[1]))
