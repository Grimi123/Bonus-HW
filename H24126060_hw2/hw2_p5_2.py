string = input("Enter a string: ")

i = 0
while i <= len(string)+1:
	if string[i] == string[i+1]:
		while i-1>=0 and i+1 <= len(string):
			if string[i-1] == string[i+2]:
				print(string[i-1:i+3])
			i=i+1
		print(string[i:i+2])
		i = i+1
	

