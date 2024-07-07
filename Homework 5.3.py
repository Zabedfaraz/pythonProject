kph = int(input("write speed in km/h: "))
mph = int(input("write speed in m/h: "))

speed1 = kph/1.609344
speed2 = mph

if speed1 > speed2:
    print(kph, " kph is faster than ", mph, " mph")
else:
    print(mph, " mph is faster than ", kph, " kph")