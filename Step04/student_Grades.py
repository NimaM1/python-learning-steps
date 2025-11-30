import json

print("""hello and welcome to your student grades app.
      to use the app choose any option you are looking for and enter it's number.
[1] Add a new student and their grades.
[2] View all students and their grades.
[3] Calculate and display the GPA/average grade for each student.
[4] Remove a student from the list.
[5] Exit the program.
""")


def main():

    while True:
        choose = input(">>>>>> ")
        if "1" in choose:
            newStudent()
            answer = input("Do you anna do something else? ").strip().lower()
            if "y" in answer:
                continue
            elif "n" in answer:
                print("Have a good day then!! ")
                break
        if "2" in choose:
            with open("students.json", "r") as file:
                data = json.load(file)
                print(data)
            answer = input("Do you anna do something else? ").strip().lower()
            if "y" in answer:
                continue
            elif "n" in answer:
                print("Have a good day then!! ")
                break
        if "3" in choose:
            gpa()
            answer = input("Do you anna do something else? ").strip().lower()
            if "y" in answer:
                continue
            elif "n" in answer:
                print("Have a good day then!! ")
                break

        if "4" in choose:
            deleteStudent()
            answer = input("Do you anna do something else? ").strip().lower()
            if "y" in answer:
                continue
            elif "n" in answer:
                print("Have a good day then!! ")
                break

        if "5" in choose:
            print("Have a good day then!! ")
            break


def newStudent():
    name = input("Enter the new student name: ")
    math = int(input("Enter his/her math grade: "))
    science = int(input("Enter his/her science grade: "))
    literature = int(input("Enter his/her literature grade: "))
    new_student = {name: {"math": math,
                          "science": science, "literature": literature}}
    with open("students.json", "r") as file:
        data = json.load(file)
    data.update(new_student)
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


def gpa():
    name = input("which student's GPA you wanna know? ")
    with open("students.json", "r") as file:
        data = json.load(file)
    print(int(data[name]["math"] + data[name]
              ["science"] + data[name]["literature"]) / 3)


def deleteStudent():
    name = input("Enter the student name you wanna delete: ")
    with open("students.json", "r") as file:
        data = json.load(file)
    data.pop(name)
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)
    print(f"you have deleted the {name} out of your list")


main()
