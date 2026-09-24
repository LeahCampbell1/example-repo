# Request input from user for total number of students
student_total = int(input("Enter number of students registering: "))

# Iterate through range of students and request information 

for i in range(student_total):
    student_ID = input("Enter student ID: ")
    with open("reg_form.txt","a+") as file:
        file.write(student_ID + "...............\n")