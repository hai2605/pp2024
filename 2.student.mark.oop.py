#Create Student class
class Student: 
    def __init__(self, studentID, studentName, DoB):
        self.id = studentID
        self.name = studentName
        self.dob = DoB
        self.marks = {}

    #intput marks for students   
    def inputMarks(self, course):
        self.marks[course.id] = input(f"Enter marks for {self.name} in {course.name}: ")
    
    #display marks of students
    def displayMarks(self, course):
        if course.id in self.mark:
            return f"{self.name} - {course.name}: {self.marks[course.id]}"
        else:
            return f"{self.name} - {course.name}: No mark available"
        
    
        
#Create Course class      
class Course:
    def __init__(self, courseID, courseName):
        self.id = courseID
        self.name = courseName

#Input number of item
def inputNumOfItem (item):
    if item == "student":
        numOfStudent = int(input("Enter the number of students: "))
        return numOfStudent
    elif item == "course":
        numOfCourse = int(input("Enter the number of courses: "))
        return numOfCourse   

#Input item infor
def inputItemInfor (item):
    if item == "student":
        studentID = input(f"Enter student's ID: ")
        studentName = input(f"Enter student's name: ")
        studentDOB = input(f"Enter student's date of birth: ")
        return {'id': studentID, 'name': studentName, 'dob': studentDOB, 'mark': {}}
    elif item == "course":
        courseID = input(f"Enter course's ID: ")
        courseName = input(f"Enter course's name: ")
        return {'id': courseID, 'name': courseName}       

# #Select item
# def selectItem(item):
#     if item == "student":
#         studentID = int(input("Enter student's ID: "))
#         return studentID
#     elif item == "course":
#         courseID = int(input("Enter course's ID: "))
#         return courseID   

#Display list of items
def listItem (item, itemList):
    if item == "student":
        if len(itemList) == 0:
            print(f"There aren't any students")
        else:
            print(f"Here is the student list:")
            for i, student in enumerate(itemList):
                print(f"{i+1}. {student.id} - {student.name} - {student.dob}")
    elif item == "course":
        if len(itemList) == 0:
            print(f"There aren't any courses")
        else:
            print(f"Here is the course list:")
            for i, course in enumerate(itemList):
                print(f"{i+1}. {course.id} - {course.name}")

def main():
    students = []
    courses = []

    numOfStudent = inputNumOfItem('student')
    for i in range(numOfStudent):
        studentInfor = inputItemInfor('student')
        students.append(Student(studentInfor['id'], studentInfor['name'], studentInfor['dob']))

    numOfCourse = inputNumOfItem('course')
    for i in range(numOfCourse):
        courseInfor = inputItemInfor('course')
        courses.append(Course(courseInfor['id'], courseInfor['name']))

    while True:
        print("1. Select Course and Input Marks")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            courseID = int(input("Enter course's ID: "))
            studentID = int(input("Enter student's ID: "))
            student = next((s for s in students if s.id == studentID), None)
            if student:
                course = next((c for c in courses if c.id == courseID), None)
                if course:
                    student.inputMarks(course)
                else:
                    print("Course not found!")
            else:
                print("Student not found!")
    
        elif choice == '2':
            listItem('course', courses)

        elif choice == '3':
            listItem('student', students)

        elif choice == '4':
            courseID = int(input("Enter course's ID: "))
            studentID = int(input("Enter student's ID: "))
            student = next((s for s in students if s.id == studentID), None)
            if student:
                course = next((c for c in courses if c.id == courseID), None)
                if course:
                    print(student.displayMarks(course))
                else:
                    print("Course not found!")
            else:
                print("Student not found!")

        elif choice == '5':
            print("Exiting Program")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")



if __name__ == "__main__":
    main()