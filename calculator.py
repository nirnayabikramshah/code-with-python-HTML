 # --- I am trying to make a calculator ---
num1 = float(input('Enter an  Number : ')) # --- This is for the first number ---
num2 = float(input('Enter another Number :' )) # --- This is for the second number ---
result = input('What do you want to do?(-,+,/,*,):') # --- This is here so that you can enter a symbol ---
if result == '+' :
    print(num1 + num2)
elif result == '-' :
    print (num1 - num2)
elif result == '*' :
    print (num1 * num2)
elif result == '/' :
    if num2 == 0:
        print("Error: You can't divide by zero! Try a different number.") # --- this will print Error if the second number is 0 ---
    else: # --- Only works if the second number is not 0 ---
        print (num1 / num2)
 # --- Now it should print the result  or the  number you want ---
 # --- I wall add UI/UX when i learn how to make a good UI/UX ---