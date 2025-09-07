# Student Gradebook System
students = []
marks = []

num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

# Input section
for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    for j in range(num_subjects):
        mark = float(input(f"Enter mark for subject {j+1}: "))
        marks.append(mark)
    students.append((name, marks))

# Output section
print("\n--- Report ---")
for name, marks in students:
    total = sum(marks)
    average = total / len(marks)
    print(f"Student: {name}, Total: {total}, Average: {average:.2f}")
