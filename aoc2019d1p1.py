'''numbers = open('Input2.txt', 'r')
nu = numbers.readlines()
number = []
number2 = []
total = 0
for x in nu:
	number.append(x.strip())
for z in number:
	number2.append(int(z))
print(number2)
for y in number2:
	if y%3 == 0:

		total = total + (y/3 - 2)
	else:
		total = total + ((y - (y%3))/3 - 2)
print(total)'''


numbers = open('Input2.txt', 'r')
nu = numbers.readlines()
number = []
number2 = []
total = 0
bruh = 0
for x in nu:
	number.append(x.strip())
for z in number:
	number2.append(int(z))
print(number2)
for y in number2:
	bruh = y
	while bruh >= 0:
		if y%3 == 0:
			bruh = (bruh/3 - 2)
			if bruh >= 0:
				total = total + bruh
				print(bruh)
		else:
			bruh = ((bruh - (bruh%3))/3 - 2)
			if bruh >= 0:	
				total = total + bruh
				print(bruh)
print(total)