a = input()
b = input()
c = a+a
if b in c or b in a[::-1]:
    print("Yes")
else:
    print("No")

#Ես սա գտել եմ սա մի կայքում, կուզեի իմանալ իմ գրածից էֆեկտիվ ա։
x = input()
y = input()

def check(x, y):
	m = len(x)
	if m != len(y):
		return False
	for i in range(m):
		x = x[1:] + x[0]
		if x == y:
			return True
	return False


if __name__ == '__main__':
	if check(x, y):
		print("Given Strings can be derived from each other")
	else:
		print("Given Strings cannot be derived from each other")
