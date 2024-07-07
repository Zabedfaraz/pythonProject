x = int(input("Welcome!..\n"
              "1) Fahrenheit to Celsius\n"
              "2) Celsius to Fahrenheit\n\n"
              "Write 1 or 2 for your desired service: "))
if x == 1:
    f = float(input("Write the temperature in fahrenheit: "))
    f2c = round((f - 32) * (5/9), 2)
    print("The temperature is ", f2c, " degree celsius")
elif x == 2:
    c = float(input("Write the temperature in celsius: "))
    c2f = round((c * (9/5)) + 32, 2)
    print("The temperature is ", c2f, " degree fahrenheit")



