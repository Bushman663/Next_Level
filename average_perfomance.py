#a program that calculates the average marks obtained in a classroom.
def average_perfomance():
    no_of_students = int(input("Enter the number of students in the class: "))
    total_marks = (0)

    for marks in range(no_of_students):
        marks = int(input("Enter the marks obtained by each students: "))
        total_marks += marks
        average_marks = total_marks/no_of_students
        average_marks = round(average_marks, 3)
    print(f"The class average marks is {average_marks}")


average_perfomance()
                         
