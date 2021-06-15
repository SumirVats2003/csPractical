# python program to find if the string is palindrome or not

st1 = input("Enter string: ")
m = len(st1)
for i in range(m):
	if st1[i] != st1[(m-1)-i]:
		print("String is not a palindrome")
		break

else:
	print("String is a palindrome")