name = input("Enter your name: ")
roll_no = int(input("Enter your roll number: "))

subject = ["English", "Hindi", "Maths", "Science", "Social Science"]

marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks for {subject[i]}: ")))

total_marks = sum(marks)
percentage = (total_marks/500)*100

#Grade calculation
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

#display result
result = "PASS" if percentage >= 40 else "FAIL"

#display report card
print("\n" + "=="*20)
print("Report Card")
print("="*20)
print("Student Name: ", name)
print("Roll Number: ", roll_no)
print("-"*20)

for i in range(5):
    print(f"{subject[i]}: {marks[i]}")

print("-"*20)
print("Total Marks: ", total_marks)
print("Percentage: ", percentage)
print("Grade: ", grade)
print("Result: ", result)
print("=="*20)