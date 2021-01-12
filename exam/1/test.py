# For year = 1905, the output should be
# centuryFromYear(year) = 20;
# For year = 1700, the output should be
# centuryFromYear(year) = 17.


def enturyFromYear(year):

    if type(year) == int and 1 <= year <= 2005:

        if year % 100 == 0:
            return int(year/100)

        if year < 100:
            return 1

        return (int(year/100)+1)
    else:
        return "You input incorrect data"


# print(enturyFromYear("1905"))
print(enturyFromYear(1905))
print(enturyFromYear(1700))
