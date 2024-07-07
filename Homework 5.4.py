a = int(input("Write the value of a: "))
b = int(input("Write the value of b: "))
c = int(input("Write the value of c: "))

d = b**2 - (4 * a * c)

if d > 0:
    print("discriminant = ", d,"\n"
          "The nature of the roots of quadratic equation is 'real and distinct'")
elif d == 0:
    print("discriminant = ", d,"\n"
          "The nature of the roots of quadratic equation is 'real and equal'")
elif d < 0:
    print("discriminant = ", d,"\n"
          "The nature of the roots of quadratic equation is 'complex and distinct'")

