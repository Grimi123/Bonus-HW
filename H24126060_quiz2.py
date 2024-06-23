money = float(input("Enter the shopping amount: "))
who = input("Enter the membership level (Regular or Gold): ")

if who =="Regular":             
	if money > 1000:#如果為regular,大於1000則開始取位於什麼區間
		if money <= 2000:
			new = money*0.9
		elif money <= 3000:
			new = money*0.85
		else:
			new = money*0.80
	else:
		new = money
	print(who+" ",new,sep="$")#輸出身分以及最後金額
elif who =="Gold":
	if money > 1000:#如果為gold,大於1000則開始取位於什麼區間
		if money <= 2000:
			new = money*0.85
		elif money <= 3000:
			new = money*0.80
		else:
			new = money*0.75
	else:
		new = money
	print(who+" ",new,sep="$")#輸出身分以及最後金額
else:
	print("Invalid membership level. Please enter 'Regular' or 'gold'.")#如果身分不為regular或gold 則輸出不合理
			
