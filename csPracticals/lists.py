# python program that generates a list containing squares of the numbers from 1 to n

a = []
n = int(input("Enter the number n: "))

for i in range(1, n+1):
	m = i*i
	a.append(m)

print(a)