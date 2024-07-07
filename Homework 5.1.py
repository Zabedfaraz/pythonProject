x = float(input("Write the principal amount: "))
r = float(input("Write the interest rate: "))
n = float(input("Write the time in years: "))
a = float(input("Write the reference amount: "))

i = x * (r/100)

if i > a:
    print("The interest is ", i, ", which is greater than the reference value")
else:
    print("The interest is ", i)


