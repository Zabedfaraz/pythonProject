length = int(input("Write length: "))
width = int(input("Write width: "))

if length > width:
    area_of_rectangle = length * width
    perimeter_of_rectangle = (length + width) * 2


    print("area of rectangle is", area_of_rectangle)
    print("perimeter of rectangle is", perimeter_of_rectangle)

else:
     print("provided length is less than width. PLease provide correct length and width")

