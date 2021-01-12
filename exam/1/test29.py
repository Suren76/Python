def circleOfNumbers(n, firstNumber):
    return int(firstNumber+(len(range(n)))/2) if firstNumber < len(range(n))/2 else int(abs(firstNumber-(len(range(n)))/2))

print(circleOfNumbers(10,5))