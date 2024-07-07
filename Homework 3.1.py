x = int(input("Write the 1st side length: "))
y = int(input("Write the 2nd side length: "))
z = int(input("Write the 3rd side length: "))


while x < y + z and y < x + z and z < x + y:
    if x == y == z:
        print("An equilateral triangle can be formed with the given measurements")
        break
    elif x == y or y == z or x == z:
        print("An Isosceles triangle can be formed with the given measurements")
        break
    else:
        print("A scalene triangle can be formed with the given measurements")
        break

else:
    print("A triangle cannot be formed with the given measurements")
