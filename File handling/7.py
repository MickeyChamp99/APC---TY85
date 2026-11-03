file = open("student.txt", "r")

data = file.read()
print("Total characters:", len(data))

file.close()