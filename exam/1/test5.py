# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.

statues = [6, 2, 3, 8]


def makeArrayConsecutive2(statues):

    if type(statues) == list and 1 <= len(statues) <= 10:

        for elm in statues:
            if type(elm) != int or elm not in range(0, 21):
                return "You input incorrect data"

        return (len(range(min(statues), max(statues)+1))-len(statues))
        
    else:
        return "You input incorrect data"


print(makeArrayConsecutive2(statues))
