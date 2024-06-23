second = 9  #令第二個乘數為second

while second >= 3: #只要second大於等於3時
	first = 9
	while first >= 1:  #只要first大於等於時
		print(first,'x',second,'=',first*second,end="\t")   #print第一列的第一組乘數 
		print(first,'x',second-1,'=',first*(second-1),end="\t")  #print第一列的第二組乘數
		print(first,"x",second-2,'=',first*(second-2),end="\n")	 #print第一列的第三組乘數
		first = first - 1  #第一乘數減一
	print() #換下一列
	second = second - 3 #第二乘數減三

