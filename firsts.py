# Student Management System

students = []

def add_student():
    name = input("Student ka naam likho: ")
    roll = input("Roll number likho: ")
    marks = int(input("Marks likho: "))
    
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    
    students.append(student)
    print("✅ Student add ho gaya\n")

def view_students():
    if not students:
        print("❌ Koi student nahi hai\n")
        return
    
    print("\n📋 Student List:")
    print("----------------------")
    for s in students:
        print("Name :", s["name"])
        print("Roll :", s["roll"])
        print("Marks:", s["marks"])
        print("----------------------")
    print()

def search_student():
    roll = input("Search ke liye roll number likho: ")
    found = False
    
    for s in students:
        if s["roll"] == roll:
            print("\n🎯 Student Mil Gaya")
            print("Name :", s["name"])
            print("Roll :", s["roll"])
            print("Marks:", s["marks"])
            found = True
            break
    
    if not found:
        print("❌ Student nahi mila\n")

def delete_student():
    roll = input("Delete ke liye roll number likho: ")
    
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("🗑️ Student delete ho gaya\n")
            return
    
    print("❌ Student nahi mila\n")

def main_menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Apna choice chuno (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("🙏 Program band ho raha hai")
            break
        else:
            print("❌ Galat choice\n")

# Program start
main_menu()