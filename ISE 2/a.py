s = input("Enter a string: ")

max_char = max(s, key=s.count)

print("Most frequent character:", max_char)
print("Frequency:", s.count(max_char))