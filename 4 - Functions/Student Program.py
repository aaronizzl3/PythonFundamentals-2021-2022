
def Create_Student(name, age, course):
    student = {
        "Name": name,
        "Age": age,
        "Course": course
    }
    return student


def Print_Student_Details(data):
    print(f"Name: {data['Name']}\n"
          f"Age: {data['Age']}\n"
          f"Course: {data['Course']}")


def How_Old_Next_Year(data):
    print(f"The student will be {data['Age'] + 1} next year.")


student_one = Create_Student("Aaron Hussain", 28, "Computing")
Print_Student_Details(student_one)
How_Old_Next_Year(student_one)



