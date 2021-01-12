def commonCharacterCount(s1, s2):
    
    if type(s1) == str and 1<=len(s1)<=15 and type(s2) == str and 1<=len(s2)<=15:
        count = []
        for char in set(s1):
            if char in s2:
                count.append([s1.count(char),s2.count(char)])

        comm_char = 0
        for _ in count:
            comm_char +=min(_)

        return comm_char


print(commonCharacterCount("aabcc", "adcaa"))
