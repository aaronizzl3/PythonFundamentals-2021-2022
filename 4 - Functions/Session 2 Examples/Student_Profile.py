
"""

Function which creates a student data model.

Function which prints out the student profile.


"""


def create_student(name, age, course):
    data_model = {
        "name": name,
        "age": age,
        "course": course
    }
    return data_model


def print_full_profile(data):
    print(f"Name: {data['name']}\n"
          f"Age: {data['age']}\n"
          f"Course: {data['course']}\n")


def change_course(data):
    new_course = input("What is your new course of study?")
    data['course'] = new_course
    return data


student_one = create_student("Aaron Hussain", 28, "Computing")
student_two = create_student("Murray Lambert", 31, "Games Technologies")

print_full_profile(student_one)
print_full_profile(student_two)

student_one = change_course(student_one)
