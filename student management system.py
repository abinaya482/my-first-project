students = []

def add_student():
    roll = input("Enter Roll Number:")

    for student in students:
        if student["Roll"] == roll:
            print("student with this Roll Number already exists")
            return

    name = input("Enter Name:")
    age = input("Enter Age:")
    course = input("Enter Course:")

    student = {
        "Roll" : roll,
        "Name" : name,
        "Age" : age,
        "Course" : course,
    }

    students.append(student)
    print("student added successfully!\n")

def view_student():
    if not students:
      print("No student record found.\n")
      return
    
    print("\nstudent record")
    print("-" * 50)
    for student in students:
        print(f"Roll : {student['Roll']} ")
        print(f"Name : {student['Name']} ")
        print(f"Age : {student['Age']} ")
        print(f"Course : {student['Course']} ")
        print("-" * 50)

def search_student():
    roll = input("Enter Roll Number to search:")

    for student in students:
        if student["Roll"] == roll:
            print("\nstudent found")
            print(student)
            return
        
        print("stdent not found.\n")

def update_student():
    roll = input("Enter Roll Number to update:")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name:")
            student["Age"] = input("Enter New Age:")
            student["Course"] = input("Enter New Course:")
            print("student updated successfully!\n")
            return
        
        print("student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete:")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("student deleted successfully!\n")
            return
        
        print("student not found.\n")

while True:
    print("====student management system====")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student ")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Student Management System...")
        break
    else:
        print("Invalid choice! Please try again.")
