x = int(input("write the 1st number: "))
y = int(input("write the 2nd number: "))
z = int(input("write the 3rd number: "))

numbers = [x, y, z]

print(sorted(numbers)[-1], " is the largest of the given numbers")
print(sorted(numbers)[0], " is the smallest of the given numbers")