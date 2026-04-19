name = input("Enter your name: ")
print("Hello", name)
math = floar(input("Math marks: "))
science = float(input("Science marks: "))
english = float(input("English marks: "))

total = math + science + english
percentage = total / 3

print("Total:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
else:
    print("Grade: C")