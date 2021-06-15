# python program that reads a file using with block and changes mode of opening

with open("python.txt", "w") as f:
	# print(f.read())
	f.write("This is appended using python\n")
	# print(f.read())


with open("python.txt") as f:
	print(f.read())

