#create a program that prints the user to enter a number of student and
#number of subjects then determine each student's average
number_students = int(input("Enter a number of students:"))
number_subject = int(input("Enter number of subject:"))
for student in range(1,number_subject+1):
    print(f"student{student}")
    print('-----------------------')
    total = 0
    for subj_num in range(1,number_subject+1):
        score = float(input(f"Enter subject {subj_num}:"))
        total = total + score
    print("-----------------------------------")
    print(f"the toatl marks is {total}")
    print(f"student average is {total/number_subject}")
    print()

