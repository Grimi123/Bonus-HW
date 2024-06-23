print("Welcome to the simple calculator program!")

while True:  #迴圈: 當最後回答要再一次則重新執行下列動作
	first = float(input("Enter the first number: "))
	second = float(input("Enter the second number: "))
	which = input("Select an arithmetic operation (+, -, * , /): ")

	if which == "+":
		result = first + second
	elif which == "-":
		result = first - second
	elif which == "*":
		result = first * second
	elif which == "/":
		if second == 0:
			print("Error: Division by zero!")
			continue  #分母為零時直接重新輸入新的數字
		else: result = first / second
	print("Result:",result)

	repeat = input("Do you want to perform another calculation? (yes of no): ")
	if repeat == "no": #回答yes則為true重新來一次 no則停止迴圈
		break
print("Goodbye!")


