numbers = input("Enter a sequence of integers separated by whitespace:")
numbers.split(" ") #分開輸入的數字並成為一個list
i = 1
first = int(numbers[0]) #讓起始數字first為list中第一位數
LICS = [first] 
FIRST = 0 #FIRST為之後出現不增遞數字的第一位
LICS_2 = [FIRST]

while i < len(numbers):
	if int(numbers[i]) > int(numbers[i-1]): #numbers下一位數字i大於前一位i-1，LICS會增加數字i
		LICS.append(int(numbers[i]))
	i = i + 1   
		
	else:
		FIRST = int(numbers[i])  #如果出現斷層，即出現不增遞數，另FIRST為第一個不增遞數
		while i < len(numbers):
			if int(numbers[i]) > int(numbers[i-1]): #numbers下一位數字i大於前一位i-1，LICS_2會增加數字i
				LICS_2.append(int(numbers[i]))
			i = i + 1
		if len(LICS_2) > len(LICS): #得出LICS與LICS_2後，如果後者長度比前者大，更新LICS為LICS_2
			LICS = LICS_2
print("Length:",len(LICS))
print("LICS:",LICS)


