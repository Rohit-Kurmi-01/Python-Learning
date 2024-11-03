Year = 200

if Year % 100 == 0 and Year % 400 == 0 :
    print("this is leap")
elif (Year % 4 == 0) and (Year % 100 != 0):
    print("this is leap year")
else:
    print(Year,"this is not leap")