# University-Management-System
University Management System
This Java program represents a console-based University Management System designed for administrative tasks. An interactive command-line interface is provided for administrators to add courses, enroll students, assign grades, and calculate overall grades.
Core Functionalities:
•	Add Course: Allows the administrator to add a new course by entering details such as course name, course code, and maximum capacity. It includes checks to prevent duplication and options to update or remove existing courses.
•	Enroll Student: Facilitates the enrollment of students into courses. It includes validation of student IDs and ensures that courses are not overbooked.
•	Assign Grades: Provides the functionality to assign grades to students for their respective courses.
•	Calculate Overall Course Grades: Computes the overall grade for students by averaging the grades received across all enrolled courses.
The system uses classes to encapsulate data and behavior, with Student, Course, and CourseManagement classes representing different entities within the university system. The code allows for updating student information through methods like enrollStudent and assignGrades, which manipulate the state of Student objects.
The Course class provides methods to update course information, such as changing the maximum capacity or removing a course.
The CourseManagement class contains static methods to manage the list of courses and the enrollment process.
Encapsulation and Access Modifiers:
•	The code uses private instance variables and public getter and setter methods to encapsulate student and course information.
•	Static variables and methods are employed to track enrollment and grade-related information across instances.
Instance Methods and Object State Manipulation:
•	Instance methods such as enrollStudent in the Student class and assignGrade in the Course class are used to manipulate object states.
Static Methods and Variables:
•	Static methods in the CourseManagement class handle operations that affect the state of the system as a whole, such as adding new courses and calculating overall grades.
In conclusion, the University Management System provides a solid foundation for managing educational administrative tasks. With its current capabilities, it serves as a functional tool for administrators. Furthermore, the implementation of persistent data storage and the implementation of additional exception handling for input validation will make this code more robust and reliable.
 

 
Reference
Eck, D. J. (2022). Introduction to programming using java version 9, JavaFX edition. Licensed under CC 4.0. 
