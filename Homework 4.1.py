x = int(input("Write the 1st number: "))
y = int(input("Write the 2nd number: "))
z = int(input("Write the 3rd number: "))


average = (x + y + z)//3
Threshold = 100
if average < Threshold:
     print("The average is ", average)
else:
     print("The average has exceeded the threshold")
