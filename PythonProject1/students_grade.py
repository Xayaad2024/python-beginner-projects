#function to calculate grade
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
#get input from the user
name = input("Enter students name:")
score = float(input("Enter the students score (0-100):"))
#validate score
if 0 <= score <= 100:
    grade = calculate_grade(score)
    print(f"{name} got grade: {grade}")
else:
    print("Invalid score:please Enter between 0-100.")
