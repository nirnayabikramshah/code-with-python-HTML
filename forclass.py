# --- Making an marks calculator ---
math = int(input('Enter the marks in math : '))
science = int(input('Enter the marks in science : '  ))
computer = int (input('Enter the marks in computer : '))
english = int(input('Enter the marks in english : '))
nepali =  int(input('Enter the marks in nepali : '))
total_marks= math + science+ computer + english + nepali
total_percentage =(total_marks /500)*100 # --- 500 because of five subjects ---
print(f"Total marks = {total_marks} ")
print(f"Total percentage = {total_percentage} % ")
# --- End ---
