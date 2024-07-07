g = str(input("welcome..\n"
              "lets calculate your body fat percentage.\n"
              "Let us know your Gender. for male press 'm' and for female press 'f': "))
a = int(input("Write your age: "))
b = int(input("Write your body weight: "))
o = int(input("Write your body fat weight: "))

assert 20 < a < 80
assert g == 'm' or g == 'f'

fp = (o/b) * 100

while g == 'm':
    if 20 < a < 39 and 8<fp<19:
        print("Your body fat percentage is ", fp, " and you have a healthy body fat percentage.")
        break
    elif 40 < a < 59 and 11<fp<21:
        print("Your body fat percentage is ", fp, " and you have a healthy body fat percentage.")
        break
    elif 60 < a < 79 and 13<fp<24:
        print("Your body fat percentage is ", fp, " and you have a healthy body fat percentage.")
        break
    else:
        print("Your current body fat percentage is unhealthy.")
        break
while g == 'f':
    if 20 < a < 39 and 21<fp<32:
        print("Your body fat percentage is ", fp, " and you have a healthy body fat percentage.")
        break
    elif 40 < a < 59 and 23<fp<33:
        print("Your body fat percentage is ", fp, " and you have a healthy body fat percentage.")
        break
    elif 60 < a < 79 and 24<fp<35:
        print("Your body fat percentage is ", fp, " and you have a healthy body fat percentage.")
        break
    else:
        print("Your current body fat percentage is unhealthy.")
        break



