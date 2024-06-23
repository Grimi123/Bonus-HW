bound = int(input("Input the range number: "))
number = 2
while number <= bound:
	i = 1 
	total = 0
	while i < number:
		if number % i == 0:
			total += i
			i += 1
		else:
			i += 1
		if i >= number:
			break
	if total == number:
		print("Perfect numbers: ", number)
	number += 1

	

