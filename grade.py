M=int(input("Enter your marks in Math : "))
S=int(input("Enter your marks in Science : "))
C=int(input("Enter your marks in Computer :  "))
avg=(M*S*C)/3
if avg >= 95 :
    print("you got an A+")
elif avg >= 90 :
    print("You got an A")
elif avg <= 89 :
    print("You got an B")
else:
    print("You got an B+")