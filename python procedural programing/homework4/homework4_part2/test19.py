#Input   Output
#5  ‘Five’
#25  ‘Twenty five’
#425  “Four hundred twenty five”
#9425  “Nine thousand four hundred twenty five”
#79425  “Seventy nine thousand four hundred twenty five”
#179425  “One hundred seventy nine thousand four hundred twenty five”


num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def n2w(n):
    for x in num2words.items():
        if x[0] == int(str(n)[:2]):
            return (x[1])
        elif x[0] > n:
            n = int(str(n)[:2])
            v = (num2words[n-n%10] + ' ' + num2words[n%10].lower())
            return v
        elif n > 90 and n < 100:
            n = int(str(n)[:2])
            v = (num2words[90] + ' ' + num2words[n%10].lower())
            return v

num = input()
x =[]
if len(num) == 6:
    if int(num[:1]) != 0:
        r = (num2words[int(num[:1])],"hundred")
        x.append(r[0])
        x.append(r[1])
    num = str(num)[1:]
if len(num) == 4 or len(num) == 5:
    if int(num[:1]) != 0:
        if len(num) == 4:
            d = (num2words[int(num[:1])],"thousand")
            x.append(d[0])
            x.append(d[1])
        if len(num) == 5:
            num1 = int(num[:2])
            d1 = (n2w(num1),"thousand")
            x.append(d1[0])
            x.append(d1[1])
            num = str(num)[1:]
    num = str(num)[1:]
if len(num) == 3:
    if int(num[:1]) != 0:
        b = (num2words[int(num[:1])],"hundred")
        x.append(b[0])
        x.append(b[1])
    num = str(num)[1:]
if len(num) <= 2 :
    num = int(num)
    x.append(n2w(num))

#x =  [x_w.lower() for x_w in x[1:]]

print(x[0]+" "+' '.join(x[1:]).lower())

