def palindromeRearranging(inputString):

    char_occur = []

    for char in set(inputString):
        char_occur.append(inputString.count(char))

    odd_occ = [_ for _ in char_occur if _ % 2]

    if len(odd_occ) > 1:
        return False
    else:
        return True

# Ավելի կարճ էլ կարաի գրեի բաըց տեսքը կտուժեր։
inputString = "aabb"

print(palindromeRearranging(inputString))
