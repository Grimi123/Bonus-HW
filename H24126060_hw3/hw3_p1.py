n = int(input("Input the total number of students (n>0) :"))

people = list(range(1,n+1))
i = 2
k = 0

while len(people)>1:
	q = i-k
	if q >= len(people):
		q = q % len(people) - 1
	people.pop(q)
	i += 3
	k += 1
	

print("The student ID who is the last one sitting on the round table:", people[0])

		








