def depositProfit(deposit, rate, threshold):

    year = 0

    while deposit < threshold:
        deposit = deposit + ((deposit/100)*rate)
        year += 1

    return year

print(depositProfit(100,2,230))