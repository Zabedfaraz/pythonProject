x = int(input("Write the 1st angle degree: "))
y = int(input("Write the 2nd angle degree: "))
z = int(input("Write the 3rd angle degree: "))


assert x > 0 and y > 0 and z > 0

while x + y + z == 180:
    if x > 90 or y > 90 or z > 90:
        print("A obtuse triangle can be formed with the given measurements")
        break
    elif x == 90 or y == 90 or z == 90:
        print("A right angled triangle can be formed with the given measurements")
        break
    else:
        print("An acute triangle can be formed with the given measurements")
        break

else:
    print("A triangle cannot be formed with the given measurements")
