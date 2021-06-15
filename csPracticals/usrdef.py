# python program that illustrates the use of a userdefined function

def findMax(lst):
	maxnum = 0
	for i in lst:
		if(i > maxnum):
			maxnum = i
		else :
			pass

	return maxnum


n = int(input("How many numbers to enter: "))
a = []
for i in range(n):
	num = int(input("Enter number: "))
	a.append(num)

m = findMax(a)
print("Max:", m)
