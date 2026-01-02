# ================================
# Student Management System
# ================================

students = {}   # dictionary to store student data


# ---------- Functions ----------

def add_student():
    roll = input("Enter roll number: ")
    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

    students[roll] = {
        "name": name,
        "marks": marks
    }
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student List ---")
    for roll, data in students.items():
        print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")


def search_student():
    roll = input("Enter roll number to search: ")
    if roll in students:
        data = students[roll]
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
    else:
        print("Student not found.")


def update_marks():
    roll = input("Enter roll number to update marks: ")
    if roll in students:
        new_marks = float(input("Enter new marks: "))
        students[roll]["marks"] = new_marks
        print("Marks updated successfully.")
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def save_to_file():
    with open("students.txt", "w") as file:
        for roll, data in students.items():
            file.write(f"{roll},{data['name']},{data['marks']}\n")
    print("Data saved to file.")


def load_from_file():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                students[roll] = {
                    "name": name,
                    "marks": float(marks)
                }
        print("Data loaded from file.")
    except FileNotFoundError:
        print("No saved file found.")


# ---------- Main Program ----------

def main():
    load_from_file()

    while True:
        print("\n====== Student Management Menu ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Save & Exit")

        choice = input("Enter your choice (1-6): ")

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
            save_to_file()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
main()
