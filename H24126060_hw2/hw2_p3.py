year = int(input("Please input Year: "))
month = int(input("Please input Month: "))

a = (year-1) // 4   #西元1年1月1日為星期一
b = (year-1) % 4
if b != 0:
	days_1 = a*(365*3 + 366) + b*365
else:
	days_1 = a*(365*3 + 366)

c = year % 4 

if month in {1,3,5,7,9,11}:
	if c == 0:
		if month > 2:
			days_2 = (month//2)*31 + (month//2 - 1)*30 + 29
		if month == 2:
			days_2 = 31
		else:
			days_2 = 0
	if c != 0:
		if month > 2:
			days_2 = (month//2)*31 + (month//2 - 1)*30 + 28
		if month == 2:
			days_2 = 31
		else:
			days_2 = 0
if month in {2,4,6,8,10,12}:
	if c == 0:
		if month > 2:
			days_2 = (month//2)*31 + (month//2 - 2)*30 + 29
		if month == 2:
			days_2 = 31
		else:
			days_2 = 0
	if c != 0:
		if month > 2:
			days_2 = (month//2)*31 + (month//2 - 2)*30 + 28
		if month == 2:
			days_2 = 31
	else:
		days_2 = 0
day = days_1 + days_2
	
first_date_of_month = (day + 1) % 7   #1為星期一

print("Sun Mon Tue Wed Thu Fri Sat")

if month == 2:
	print("    "*(first_date_of_month+2), end = "")
else:
	print("    "*first_date_of_month, end = "")

i = 1
if month ==2:
	while True:
		print("%02d" % i, end = "  ")
		i = i + 1
		if i > 5 - first_date_of_month:
			break
else:
	while True:
		print("%02d" % i, end = "  ")
		i = i + 1
		if i > 7 - first_date_of_month:
			break
print()

j = i

if month in {1,3,5,7,8,10,12}:
	while i <31:
		while i < j+7:
			print("%02d" % i, end = "  ")
			i = i + 1
			if i > 31:
				break
		print()
		j = j + 7
i = 7 - first_date_of_month + 1
j = i
if month in {4,6,9,11}:
	while i <=30:
		while i < j+7:
			print("%02d" % i, end = "  ")
			i = i + 1
			if i >30:
				break
		print()
		j = j + 7	
i = 7 - first_date_of_month + 1 - 2
j = i
if month == 2:
	if year % 4 ==0:
		while i <=29:
			while i < j+7:
				print("%02d" % i, end = "  ")
				i = i + 1
				if i >29:
					break
			print()
			j = j + 7
	else:
		while i <=28:
			while i < j+7:
				print("%02d" % i, end = "  ")
				i = i + 1
				if i >28:
					break
			print()
			j = j + 7