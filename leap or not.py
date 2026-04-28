year=int(input("Enter an year : " ))
divisor=4
divisible=[]
# --- Leap year or not ---
# --- If the year is divisible by 4 it is a leap year ---
if year % divisor == 0 :
    divisible.append(year)
    print("Leap year")
else:
    print("Not a leap year")
