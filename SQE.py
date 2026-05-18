students = {}
def add_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Student already exists")
        return

    name = input("Enter student name: ")

    try:
        math = float(input("Enter Math marks: "))
        english = float(input("Enter English marks: "))
        science = float(input("Enter Science marks: "))

    except ValueError:
        print("Please enter valid numbers")
        return

    if math < 0 or math > 100:
        print("Invalid Math marks")
        return

    if english < 0 or english > 100:
        print("Invalid English marks")
        return

    if science < 0 or science > 100:
        print("Invalid Science marks")
        return

    students[roll] = {
        "name": name,
        "marks": [math, english, science]
    }

    print("Student added successfully")


def view_students():
    if not students:
        print("No students found")
        return

    for roll in students:
        data = students[roll]
        avg = sum(data["marks"]) / 3

        print("\nRoll Number:", roll)
        print("Name:", data["name"])
        print("Marks:", data["marks"])
        print("Average:", round(avg, 2))


def search_student():
    roll = input("Enter roll number: ")

    if roll in students:
        data = students[roll]
        avg = sum(data["marks"]) / 3

        print("\nStudent Found")
        print("Name:", data["name"])
        print("Marks:", data["marks"])
        print("Average:", round(avg, 2))

    else:
        print("Student not found")


def update_marks():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found")
        return

    try:
        math = float(input("Enter new Math marks: "))
        english = float(input("Enter new English marks: "))
        science = float(input("Enter new Science marks: "))

    except ValueError:
        print("Please enter valid numbers")
        return

    if math < 0 or math > 100:
        print("Invalid Math marks")
        return

    if english < 0 or english > 100:
        print("Invalid English marks")
        return

    if science < 0 or science > 100:
        print("Invalid Science marks")
        return

    students[roll]["marks"] = [math, english, science]
    print("Marks updated successfully")


def delete_student():
    roll = input("Enter roll number: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully")
    else:
        print("Student not found")


def generate_report():
    if not students:
        print("No students found")
        return

    print("\nSTUDENT REPORT")

    for roll in students:
        data = students[roll]
        avg = sum(data["marks"]) / 3

        if avg >= 80:
            grade = "A"
        elif avg >= 65:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"

        print("\nRoll Number:", roll)
        print("Name:", data["name"])
        print("Average:", round(avg, 2))
        print("Grade:", grade)


if __name__ == "__main__":
    while True:
        print("\nSTUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Generate Report")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            generate_report()
        elif choice == "0":
            print("Thank you for using the system")
            break
        else:
            print("Invalid choice")