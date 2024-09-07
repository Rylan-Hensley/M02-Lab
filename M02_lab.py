#Rylan Hensley
#GPA list Outputter
#This program will output whether a student has made the Dean's list or Honor role based on the GPA

last_name = input('Input last name: ')

if last_name != 'ZZZ':
    first_name = input('Input first name: ')
    gpa = float(input('Enter GPA: '))
    if gpa >= 3.5:
        print("Student has made the Dean's.")
    elif gpa >= 3.25:
        print("Student has made the Honor Roll.")
