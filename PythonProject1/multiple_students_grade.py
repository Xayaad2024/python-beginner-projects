from webbrowser import Elinks

while True:
    name = input("Enter students name (or type 'done' to finish):")
    if name.upper() == 'done':
        break
    score = float(input("Enter score for " + name + ":"))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(name +" got grade:",grade)