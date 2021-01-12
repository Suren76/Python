def revers(number):
    def reverse(num, r=0):
        if num == 0:
            return r
        return reverse(num // 10, r * 10 + num % 10)

    return reverse(number)


print(revers(2))
print(revers(13))
print(revers(815796))
print(revers(1000))
