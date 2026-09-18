class Student:
    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def display(self):
        print(
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Course: {self.course} | "
            f"Marks: {self.marks}"
        )


students = []


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = Student(student_id, name, course, marks)
    students.append(student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent Records")
    print("-" * 60)

    for student in students:
        student.display()


def search_student():
    student_id = input("Enter student ID to search: ")

    for student in students:
        if student.student_id == student_id:
            student.display()
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
