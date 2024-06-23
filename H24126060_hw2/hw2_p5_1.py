a = 0
b = 1
n = int(input("Enter a non-negative integer n: "))

if n == 0:
	result = a 
elif n == 1:
	result = b
else:
	i = 2
	while i <= n:
		result = a + b
		a = result
		b = a
		i = i + 1
k = result
print("The %d‐th Fibonacci sequence number is %d" % (n , k))
			
			