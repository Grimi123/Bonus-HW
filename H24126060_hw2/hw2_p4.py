layers = int(input("Enter the number of layers (2 to 5) = "))
top = int(input("Enter the side length of the top layer (2 to 6) = "))
gorwth = int(input("Enter the growth of each layer (1 to 5) = "))
width = int(input("Enter the trunk width (odd number, 3 to 9) = "))
height = int(input("Enter the trunk hieght (4 to 10) = "))

i=1
mid = top+gorwth*(layers-1)
print(" "*(mid-i),"#",sep = "")

bound_a = (top-2)*2-1
b=1

while True:
	i=2
	a=1
	while True:
		if bound_a < a:		
			print(" "*(mid-i),"#"*(a+2), sep = "")
			break
		print(" "*(mid-i),"#","@"*a,"#", sep = "")	
		i = i + 1
		a = a + 2
	bound_a = bound_a + gorwth*2
	if b == layers:
		break
	b = b +	1

j = 1
while True:
	print(" "*(mid - width//2 - 1), "|"*width, sep = "")
	j = j + 1
	if j > height:
		break