unit_used=int(input("enter the used unit = "))
if unit_used <= 20:
 print("You have to pay Rs.30 ")
elif  21 <= unit_used <=45 :
 print("You have to pay Rs." , unit_used * 5)
else:
 print("You have to pay Rs.", unit_used * 7)