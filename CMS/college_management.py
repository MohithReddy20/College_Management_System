import json

# Base Class for common attributes
class Person:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    def get_details(self):
        return f"Name: {self.name}, Mobile: {self.mobile}"

# Student Class inheriting from Person
class Student(Person):
    def __init__(self, name, mobile, roll_number, branch):
        super().__init__(name, mobile)
        self.roll_number = roll_number
        self.branch = branch

    def get_student_details(self):
        return f"{self.get_details()}, Roll Number: {self.roll_number}, Branch: {self.branch}"

# Teacher Class inheriting from Person
class Teacher(Person):
    def __init__(self, name, mobile, subject):
        super().__init__(name, mobile)
        self.subject = subject

    def get_teacher_details(self):
        return f"{self.get_details()}, Subject: {self.subject}"

# College Class to manage students and teachers
class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def view_students(self):
        if self.students:
            for student in self.students:
                print(student.get_student_details())
        else:
            print("No students added yet.")

    def view_teachers(self):
        if self.teachers:
            for teacher in self.teachers:
                print(teacher.get_teacher_details())
        else:
            print("No teachers added yet.")

    def search_students(self, search_term):
        found_students = [student for student in self.students if search_term.lower() in student.name.lower() or search_term in str(student.roll_number)]
        if found_students:
            for student in found_students:
                print(student.get_student_details())
        else:
            print("No students found with that name or roll number.")

    def search_teachers(self, search_term):
        found_teachers = [teacher for teacher in self.teachers if search_term.lower() in teacher.name.lower()]
        if found_teachers:
            for teacher in found_teachers:
                print(teacher.get_teacher_details())
        else:
            print("No teachers found with that name.")

# Save data to file for persistence
def save_data(colleges):
    data = []
    for college in colleges:
        college_data = {
            'college_name': college.college_name,
            'students': [{'name': student.name, 'mobile': student.mobile, 'roll_number': student.roll_number, 'branch': student.branch} for student in college.students],
            'teachers': [{'name': teacher.name, 'mobile': teacher.mobile, 'subject': teacher.subject} for teacher in college.teachers]
        }
        data.append(college_data)

    with open('colleges_data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Load data from file
def load_data():
    try:
        with open('colleges_data.json', 'r') as file:
            data = json.load(file)
            colleges = []
            for college_data in data:
                college = College(college_data['college_name'])
                for student_data in college_data['students']:
                    student = Student(student_data['name'], student_data['mobile'], student_data['roll_number'], student_data['branch'])
                    college.add_student(student)
                for teacher_data in college_data['teachers']:
                    teacher = Teacher(teacher_data['name'], teacher_data['mobile'], teacher_data['subject'])
                    college.add_teacher(teacher)
                colleges.append(college)
            return colleges
    except FileNotFoundError:
        return []

# Show Menu for the console interface based on user role
def show_menu(user_role):
    options = []
    if user_role == 'admin':
        options = [
            "Add College",
            "Add Student",
            "Add Teacher",
            "View Students",
            "View Teachers",
            "Search Students",
            "Search Teachers",
            "Exit"
        ]
    elif user_role == 'user':
        options = [
            "View Students",
            "View Teachers",
            "Search Students",
            "Search Teachers",
            "Exit"
        ]
    
    # Displaying the options with dynamic numbering
    print("\nAvailable Options:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    choice = input("Enter your choice: ")
    return choice, options

# Main function
def main():
    colleges = load_data()
    print("Welcome to the College Management System!")

    user_role = input("Enter your role (admin/user): ").lower()

    while True:
        choice, options = show_menu(user_role)

        try:
            choice = int(choice)
            if choice < 1 or choice > len(options):
                print("Invalid option. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if options[choice - 1] == "Add College" and user_role == 'admin':
            college_name = input("Enter college name: ")
            if any(college.college_name == college_name for college in colleges):
                print(f"College '{college_name}' already exists.")
            else:
                colleges.append(College(college_name))
                print(f"College '{college_name}' added!")

        elif options[choice - 1] == "Add Student" and user_role == 'admin':
            college_name = input("Enter college name to add student: ")
            college = next((college for college in colleges if college.college_name == college_name), None)
            if college:
                name = input("Enter student name: ")
                mobile = input("Enter student mobile: ")
                roll_number = input("Enter roll number: ")
                branch = input("Enter student branch: ")
                student = Student(name, mobile, roll_number, branch)
                college.add_student(student)
                print("Student added successfully!")
            else:
                print(f"College '{college_name}' not found.")

        elif options[choice - 1] == "Add Teacher" and user_role == 'admin':
            college_name = input("Enter college name to add teacher: ")
            college = next((college for college in colleges if college.college_name == college_name), None)
            if college:
                name = input("Enter teacher name: ")
                mobile = input("Enter teacher mobile: ")
                subject = input("Enter subject: ")
                teacher = Teacher(name, mobile, subject)
                college.add_teacher(teacher)
                print("Teacher added successfully!")
            else:
                print(f"College '{college_name}' not found.")

        elif options[choice - 1] == "View Students":
            college_name = input("Enter college name to view students: ")
            college = next((college for college in colleges if college.college_name == college_name), None)
            if college:
                college.view_students()
            else:
                print(f"College '{college_name}' not found.")

        elif options[choice - 1] == "View Teachers":
            college_name = input("Enter college name to view teachers: ")
            college = next((college for college in colleges if college.college_name == college_name), None)
            if college:
                college.view_teachers()
            else:
                print(f"College '{college_name}' not found.")

        elif options[choice - 1] == "Search Students":
            search_term = input("Enter student name or roll number to search: ")
            college_name = input("Enter college name to search in: ")
            college = next((college for college in colleges if college.college_name == college_name), None)
            if college:
                college.search_students(search_term)
            else:
                print(f"College '{college_name}' not found.")

        elif options[choice - 1] == "Search Teachers":
            search_term = input("Enter teacher name to search: ")
            college_name = input("Enter college name to search in: ")
            college = next((college for college in colleges if college.college_name == college_name), None)
            if college:
                college.search_teachers(search_term)
            else:
                print(f"College '{college_name}' not found.")

        elif options[choice - 1] == "Exit":
            print("Exiting program...")
            save_data(colleges)
            break

if __name__ == "__main__":
    main()
