# python program that illustrates the use of a builtin function

n = int(input("How many numbers to enter: "))
a = []
for i in range(n):
	num = int(input("Enter number: "))
	a.append(num)

m = max(a)
print("Maximum number is: ", m)