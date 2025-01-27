// import package
import java.util.*;
// This is the console-based University Management System, managed by an administrator.
public class AdministratorUI {
    static final Scanner scanner = new Scanner(System.in);

    // This is the entry point of the application. It runs in an infinite loop presenting the user with the menu.
    // The user's choice, entered via keyboard, is then handled within the switch-case statement.
    // After performing the requested operation, the menu is shown again. The loop ends when the user
    // enters "q" to quit the program.
    public static void main(String[] args) {
        while (true) {
            showMenu();
            String command = scanner.nextLine();
            switch (command) {
                case "1":
                    addCourse();
                    break;
                case "2":
                    enrollStudent();
                    break;
                case "3":
                    assignGrades();
                    break;
                case "4":
                    calculateOverallCourseGrades();
                    break;
                case "q":
                    System.out.println("Exiting...");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid command. Please try again.");
                    break;
            }
        }
}

// This method prints the menu of possible operations to the console.
// The user can add a new course, enroll a student, assign grades,
// calculate overall course grades, or quit the program.
private static void showMenu() {
    System.out.println("\nWelcome in the University Management System");
    System.out.println("Select an operation: ");
    System.out.println("1: Add new course");
    System.out.println("2: Enroll student");
    System.out.println("3: Assign grades");
    System.out.println("4: Calculate overall course grades");
    System.out.println("Enter 'q' to quit");
}
// ADD course method
// This method adds a new course to the university system.
// The administrator is prompted to enter the course name and code, and the maximum capacity for the course.
// If a course with the entered name already exists, the user is asked whether they want to update or remove it.
private static void addCourse() {
    System.out.println("Enter Course Name:");
    String courseName = scanner.nextLine().toLowerCase();
    // Check if the course already exists
    Course existingCourse = CourseManagement.findCourseByName(courseName);
    if (existingCourse != null) {
  System.out.println("Course already exists. Do you want to update it or remove it? (update/remove):");
    String response = scanner.nextLine();
    if ("update".equalsIgnoreCase(response)) {
        System.out.println("Enter New Maximum Capacity:");
        int newMaxCapacity = Integer.parseInt(scanner.nextLine());
        existingCourse.setMaxCapacity(newMaxCapacity);
        System.out.println("Course updated successfully.");
    } else if ("remove".equalsIgnoreCase(response)) {
        Course.remove(existingCourse);
        System.out.println("Course removed successfully.");
    } else {
        System.out.println("Invalid option. Returning to main menu.");
    }
} else {
    System.out.println("Enter Course Code:");
    String courseCode = scanner.nextLine();
    int maxCapacity = 0;
    try {
        System.out.println("Enter Maximum Capacity:");
        maxCapacity = Integer.parseInt(scanner.nextLine());
    } catch (NumberFormatException e) {
        System.out.println("Invalid input. Please enter an integer for capacity.");
    }
    // Add new course to the list
    Course newCourse = new Course(courseCode, courseName, maxCapacity);
    CourseManagement.courses.add(newCourse);
    System.out.println("Course '" + courseName + "' added successfully.");
    // I add this loop to show courses registered.
// I use this during my debug process.
        System.out.println("\nHere is the list of registered courses:");
        System.out.println(newCourse);
    }

}

// Enroll student method
// This method enrolls a student in a course. The administrator is prompted
// to enter the course code and the student's ID and name. The method does some
// validation checks and if everything checks out, the student is enrolled in the course.
private static void enrollStudent() {
    System.out.println("Enter Course Code:");
    String courseCode = scanner.nextLine().toUpperCase();
    Course course = CourseManagement.findCourseByCode(courseCode);

    if (course == null) {
        System.out.println("This course code does not exist. Please try again.");
        return;
    }
    if (!course.canEnroll()) {
        System.out.println("This course is full. Please try enrolling in a different course.");
        return;
    }
    System.out.println("Enter Student ID: (4 alphanumeric characters)");
    String studentId = scanner.nextLine().toUpperCase();
    if (!isValidStudentId(studentId)) {
        System.out.println("Invalid Student ID format. Please try again.");
        return;
    }

    System.out.println("Enter Student Name:");
    String studentName = scanner.nextLine();

    Student student = new Student(studentId, studentName);
    course.enrollStudent(student);
    System.out.println("Student successfully enrolled in the course.");
    System.out.println("\nHere is the list of enrolled students in " + course.getCourseName() + ":");
    displayEnrolledStudents(course);
}
// validation for student ID type is 4 alphanumeric characters.
private static boolean isValidStudentId(String studentId) {
    String idFormat = "^[a-zA-Z0-9]{4}$";
    return studentId.matches(idFormat);
}
// I add this during the debugs process. It displays enrolled student
private static void displayEnrolledStudents(Course course) {
    System.out.println("\nHere enrolled student");
    for (Student student : course.getStudentsEnrolled()) {
        System.out.println(student + "" + course.getCourseName());
    }
}

//Method to assign grades
// This method assigns grades to a student for a particular course.
// The administrator is prompted to enter the course code, student ID, and the grade to be assigned.
// Note: if a grade for the same course is enter multiple times, it gets overwrite each time.
private static void assignGrades() {
    System.out.println("Enter Course Code:");
    String courseCode = scanner.nextLine().toLowerCase();
    Course course = CourseManagement.findCourseByCode(courseCode);

    if (course == null) {
  System.out.println("This course code does not exist. Please try again.");
        return;
    }

    System.out.println("Enter Student ID:");
    String studentId = scanner.nextLine().toLowerCase();
    if (!isValidStudentId(studentId)) {
        System.out.println("Invalid Student ID format. Please try again.");
        return;
    }

    System.out.println("Enter Grade:");
    double grade = Double.parseDouble(scanner.nextLine());

    course.assignGrade(studentId, grade);
    System.out.println("Grade assigned successfully.");

}
// Method to calculate overall grade
// Prompt for student ID and display a list of courses graded for this student
// and provide overall grade (sum of each graded course divided the number of courses graded).
private static void calculateOverallCourseGrades() {
    System.out.println("Enter Student ID:");
    String studentId = scanner.nextLine().toLowerCase();
    if (!isValidStudentId(studentId)) {
        System.out.println("Invalid Student ID format. Please try again.");
        return;
    }

    Student student = Student.findStudentById(studentId);
    

    List<Course> gradedCourses = CourseManagement.findCoursesGradedForStudent(studentId);
    if (gradedCourses.isEmpty()) {
        System.out.println("No courses graded for this student.");
        return;
    }

    double overallGrade = 0;
    int gradedCourseCount = 0;
    StringBuilder coursesInfo = new StringBuilder();
    for (Course course : gradedCourses) {
        double grade = course.getGradeForStudent(studentId);
        // since grade is a double and double cannot be null. a -1 number out of rage grade is used instead.
        if (grade == -1) {
            System.out.println("Grade for course " + course.getCourseName() + " not found.");
            continue; // Skip this course if the grade is not assigned
        }
        overallGrade += grade;
        gradedCourseCount++;
        coursesInfo.append(String.format("{course name: %s, grades: %s}; ", course.getCourseName(), grade));
    }

    if (gradedCourseCount == 0) {
        System.out.println("No grades found for the student.");
        return;
    }

    double averageGrade = overallGrade / gradedCourseCount;
    String output = String.format("Student Name: %s, Student ID: %s, Overall grade: %.2f, Courses: %s",
            student.getName(), studentId, averageGrade, coursesInfo.toString());
    System.out.println(output);
}

// Import package
import java.util.*;
// The Student class represents a student in this course management system.
public class Course {
    private String courseCode;
    private String courseName;
    private int maxCapacity;
    private Map<String, Double> studentGrades;
    private static int totalEnrolledStudents = 0;
    // This is a list of Student objects representing all the students that are currently enrolled in this course.
    private List<Student> enrolledStudentsList = new ArrayList<>();

    // constructor
    public Course(String courseCode, String courseName, int maxCapacity) {
        this.courseCode = courseCode;
        this.courseName = courseName;
        this.maxCapacity = maxCapacity;
        this.studentGrades = new HashMap<>();
    }

    public static void remove(Course existingCourse) {
        CourseManagement.courses.remove(existingCourse);
        totalEnrolledStudents--;
    }

    public Object getCourseName() {
        return courseName;
    }

    public void setMaxCapacity(int newMaxCapacity) {
        this.maxCapacity = newMaxCapacity;
    }

    public boolean canEnroll() {
        return totalEnrolledStudents < maxCapacity;
    }

    public Object getCourseCode() {
        return courseCode;
    }
    public List<Student> getStudentsEnrolled() {
        return enrolledStudentsList;
    }

    // The toString method is overridden from the Object class.
    // It provides a custom string representation of a Course object by returning
    // a string that includes the courseCode, courseName, and maxCapacity properties.
    // I used this method during the debugs process.
    @Override
    public String toString() {
        return "Course Code: " + this.courseCode
                + ", Course Name: " + this.courseName
                + ", Maximum Capacity: " + this.maxCapacity;
    }

    // Adds a Student object to the enrolledStudentsList and increases counter of total students enrolled.
    public void enrollStudent(Student student) {
        enrolledStudentsList.add(student);
        totalEnrolledStudents++;
    }
    // This method puts a grade for a student in the studentGrades map.
    public void assignGrade(String studentId, double grade) {
        studentGrades.put(studentId, grade);
    }
    // This method attempts to return the grade for the student with the specified student ID.
    // If a grade for the student does not exist, it returns a sentinel value of -1.0.
    public Double getGradeForStudent(String studentId) {
        return studentGrades.getOrDefault(studentId, -1.0);
    }
}

// import package
import java.util.HashMap;
import java.util.Map;

//The Student class represents an entity Student in the course management system.
// It has private class level attributes studentName, studentId, enrolledCourses and grade.
public class Student {
    private static String studentName;
    private static String studentId;
    private Map<Course, String> enrolledCourses = new HashMap<>();
    private Object grade;

    // This is a contractor used to create a new student object.
    public Student(String studentId, String studentName) {
        this.studentId = studentId;
        this.studentName = studentName;
        this.enrolledCourses = new HashMap<>();
    }

    // This method is used to find the student by ID
    public static Student findStudentById(String studentId) {
        return new Student(studentId,studentName);
    }

    // This is a method to get a list of enrolled classes of a student.
    public String getEnrolledCourses() {
        StringBuilder enrolledCourses = new StringBuilder();
        for (Map.Entry<Course, String> entry : this.enrolledCourses.entrySet()) {
            enrolledCourses.append(entry.getKey().getCourseName()).append(", ");
        }
        return enrolledCourses.toString();
    }

    // override is used to print each student on to enroll method.
    @Override
    public String toString() {
        return "Student ID: " + this.studentId + ", Student Name: "
                + this.studentName + ", Enrolled Course: " + this.getEnrolledCourses();
    }

    // Method to get student id.
    public static String getStudentId() {
        return studentId;
    }
    // Method to get student name.
    public Object getName() {
        return studentName;
    }
}

// import package
import java.util.*;


public class CourseManagement {
    static List<Course> courses = new ArrayList<>();
    private static List<Student> students = new ArrayList<>();

    // This method takes a string argument courseName. It iterates through each
    // Course object in the courses list. If the course name of a particular
    // Course object matches the courseName argument, that Course object is returned,
    // otherwise null is returned. This method is used to search for a course by its name.
    public static Course findCourseByName(String courseName) {
        for (Course course : courses) {
            if (course.getCourseName().equals(courseName)) {
                return course;
            }
        }
        return null;
    }
    // This method returns a list of Course objects for which a grade has been assigned
    // to the student with the given studentId. If the student's grade for a course
    // isn't -1.0 (used as a sentinel value implying that no grade has been assigned),
    // that course is added to the gradedCourses list.
    public static List<Course> findCoursesGradedForStudent(String studentId) {
        List<Course> gradedCourses = new ArrayList<>();
        for (Course course : courses) {
            if (course.getGradeForStudent(studentId) != -1.0) { // Check if grade is assigned
                gradedCourses.add(course);
            }
        }
        return gradedCourses;
    }
    // This method searches for a Course object that has a course code matching
    // the courseCode argument. If a match is found, the matching Course object i
    // s returned, otherwise null is returned.
    public static Course findCourseByCode(String courseCode) {
        for (Course course : courses) {
            if (course.getCourseCode().equals(courseCode)) {
                return course;
            }
        }
        return null;
    }
    //This method takes studentId as a parameter and iterates through students list.
    // If a Student object with a student ID matching the studentId parameter is found,
    // it is returned, otherwise null is returned.
    public static Student findStudentById(String studentId) {
        for (Student student : CourseManagement.students) {
            if (Student.getStudentId().equalsIgnoreCase(studentId)) {
                return student;
            }
        }
        return null;
    }

}
