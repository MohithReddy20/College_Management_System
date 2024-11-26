# College Management System in Python

## Overview

The **College Management System** is a console-based application built in Python that enables efficient management of colleges, students, and teachers. The system allows users to add multiple colleges, manage student and teacher details, and perform various operations such as viewing, searching, and updating records. The application is designed with Object-Oriented Programming (OOP) principles and features role-based access for administrators and regular users.

## Features

- **Admin Features**:
  - Add multiple colleges.
  - Add students with details like roll number, name, mobile, and branch.
  - Add teachers with details including name, mobile, and subject.
  - View and search student and teacher details for specific colleges.
  
- **User Features**:
  - View and search student and teacher details.
  - No ability to add or modify records.

- **Data Persistence**: Data is stored persistently using a JSON file (`colleges_data.json`), so records are preserved even after closing and reopening the program.

## Technologies Used

- **Programming Language**: Python
- **Key Concepts**: 
  - Object-Oriented Programming (OOP) (Classes, Inheritance, Encapsulation)
  - Error Handling and Input Validation
  - File Handling (JSON for data storage)
- **Libraries**: None (Pure Python)

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/college-management-system.git
2. **Navigate to the project directory**:
   cd college-management-system
3. **Run the Python file**:
   python college_management_system.py
4. The program will start, and you can follow the on-screen prompts to interact with the system.

## Usage

Upon running the program, you will be prompted to log in as an admin or user. Based on the role you choose, the available options will differ:

# Admin Options:
Add College: Add a new college to the system.
Add Student: Add student details (name, roll number, branch) to a college.
Add Teacher: Add teacher details (name, subject) to a college.
View Students: View the list of students in a specific college.
View Teachers: View the list of teachers in a specific college.
Search Students: Search for students by name or roll number.
Search Teachers: Search for teachers by name.

# User Options:
View Students: View the list of students in a specific college.
View Teachers: View the list of teachers in a specific college.
Search Students: Search for students by name or roll number.
Search Teachers: Search for teachers by name.
# Example Output:
Welcome to the College Management System!
Enter your role (admin/user): admin

Available Options:
1. Add College
2. Add Student
3. Add Teacher
4. View Students
5. View Teachers
6. Search Students
7. Search Teachers
8. Exit

## Data Persistence
Data is saved in the colleges_data.json file, which stores the college, student, and teacher details. When the program is restarted, the data will be loaded from this file, allowing for continuous management of records across sessions.

## Challenges Faced
Handling dynamic data efficiently for multiple colleges.
Implementing role-based access to ensure proper permissions for different types of users.
Ensuring that data persists even after the program is closed.

## Future Enhancements
Graphical User Interface (GUI): Implement a GUI using Tkinter or PyQt for a more user-friendly experience.
Database Integration: Integrate a relational database like SQLite to manage data more efficiently.
Advanced Search Filters: Implement advanced search features to filter by multiple criteria (e.g., branch, subject).
Reporting: Add options to generate reports for students and teachers.

## Contributing
Feel free to fork this project and submit pull requests if you wish to contribute improvements or additional features.

## License
This project is open source and available under the MIT License.

## Contact
If you have any questions or suggestions, feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/mohith-reddy-yannam/) or [GitHub](https://github.com/MohithReddy20).
