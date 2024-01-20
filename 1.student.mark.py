#Input number of students
def numberOfStudent():
    numOfStudent = int(input("Enter the number of students: "))
    return numOfStudent

#Input number of courses
def numberOfCourse():
    numOfCourse = int(input("Enter the number of courses: "))
    return numOfCourse


#Input students' infos
def studentInfos(students, numOfStudent):
    for i in range(numOfStudent):
        print(f"Student {i+1}:")
        studentID = input("Enter the student ID: ")
        studentName = input("Enter the student's name: ")
        studentDoB = input("Enter the student's date of birth: ")
        students.append({'id': studentID, 'name': studentName, 'DoB': studentDoB, 'marks': {}})

    return students 

#Input courses' infos
def courseInfos(courses, numOfCourse):
    for i in range(numOfCourse):
        print(f"Course {i+1}:")
        courseID = input("Enter course ID: ")
        courseName = input("Enter course's name: ")
        courses.append({'id': courseID, 'name': courseName})
    
    return courses

#Select courses
def selectCourse(courses):
    print("list of courses: ")
    listCourses(courses)
    courseID = input("Enter the ID of the course selected: ")
    return courseID

# Input the student mark in a course base on the course id
def inputMark(student, course):
    student["marks"][course['id']] = input(f"Enter marks for {student['name']} in {course['name']}: ")

# Display a list of students
def listStudents(students):
    if len(students) == 0:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        for i , student in  enumerate(students):
            print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}\n")

# Display a list of courses
def listCourses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
    else:    
        print("Here is the course list: ")
        for i, course in enumerate(courses):
            print(f"{i+1}. {course['id']} - {course['name']}")

#Display marks of students
def displayMark(student, course):
    if course['id'] in student['marks']:
        print(f"{student['name']} - {course['name']}: {student['marks'][course['id']]}")
    else:
        print(f"{student['name']} - {course['name']}: No mark available")

def main():
    # Initialize the list for DATA option
    students = []
    courses = []
    
    numOfStudents = numberOfStudent()
    studentInfos(students, numOfStudents)
            
    numOfCourses = numberOfCourse()
    courseInfos(courses, numOfCourses)

    while(True):
        print("1. Select Course and Input Marks")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            courseID = selectCourse(courses)
            studentID = input("Enter student ID: ")
            student = next((s for s in students if s['id'] == studentID), None)
            if student:
                course = next((c for c in courses if c['id'] == courseID), None)
                if course:
                    inputMark(student, course)
                else:
                    print("Course not found!")
            else:
                print("Student not found!")
                    

        elif choice == '2':
            listCourses(courses)

        elif choice == '3':
            listStudents(students)

        elif choice == '4':
            courseID = selectCourse(courses)
            studentID = input("Enter student ID: ")
            student = next((s for s in students if s['id'] == studentID), None)
            if student:
                course = next((c for c in courses if c['id'] == courseID), None)
                if course:
                    inputMark(student, course)
                else:
                    print("Course not found!")
            else:
                print("Student not found!") 

        elif choice == '5':
            print("Exiting Program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Call the main function
if __name__ == "__main__":
    main()
