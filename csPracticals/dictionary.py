dict1 = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
ans = "y"

while ans == "y" or ans == "Y" :
	val = input("Enter value: ")
	print("Value", val, end = " ")
	for k in dict1:
		if dict1[k] == val:
			print("Exists at", k)
			break
	else:
		print("Not found")
	ans = input("Want to check more values? (y/n): ")