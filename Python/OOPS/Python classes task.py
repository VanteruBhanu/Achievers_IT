class Student:
    # A class is a blueprint for creating objects, i.e., instances.
    # A class contains two types: attributes and methods.
    # The starting letter of a class name should be capital.

    def __init__(self, name, email, yearofpassing, coursename, qualification):
        # The def keyword is used to initialize the function
        # init is a method which is used as a constructor. Its primary role is to initialize the newly created attributes of the project.
        # When you create an instance of the class, 'self' allows access to the attributes and methods of the instance.
        # The words mentioned inside the parenthesis are called parameters, which are used to initialize the instance attributes of the class.
        self.name = name
        self.email = email
        self.yearofpassing = yearofpassing
        self.coursename = coursename
        self.qualification = qualification

    def display_info(self):
        return (f"Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Year of passing: {self.yearofpassing}\n"
                f"Course name: {self.coursename}\n"
                f"Qualification: {self.qualification}\n")

    def Total_marks(self):
        student_marks = [
            {"subject": "Telugu", "Marks": 95},
            {"subject": "Hindi", "Marks": 85},
            {"subject": "English", "Marks": 75},
            {"subject": "Maths", "Marks": 90},
            {"subject": "Science", "Marks": 85},
            {"subject": "Social", "Marks": 95}
        ]
        total_marks_obtained = sum(marks['Marks'] for marks in student_marks)
        print("Marks Obtained:", [marks['Marks'] for marks in student_marks])
        print("Total Marks Obtained:", total_marks_obtained)

        return total_marks_obtained

    def Grade(self):
        grade_marks = self.Total_marks()
        if grade_marks >= 550:
            print("Grade Obtained: A")
        elif grade_marks >= 450 and grade_marks <= 549:
            print("Grade Obtained: B")
        elif grade_marks >= 350 and grade_marks <= 449:
            print("Grade Obtained: C")
        elif grade_marks >= 250 and grade_marks <= 349:
            print("Grade Obtained: D")
        else:
            print("You have failed.")
            
    def course_skill(self, skills):
        skills_list =",".join(skills)
        return (f"{self.name} choosen the {self.coursename} course\n"
                f"This course contains the following skills: {skills_list}")
#skills
skills = ["Python", "Data Analysis", "Web Frameworks", "Javascript", "Database Management"]


# Creating an instance of the Student class
totalinfo = Student("Bhanu", "prakashbhanu8390@gmail.com", 2024, "Python Full Stack", "Btech")

# Displaying information of the student
print(totalinfo.display_info())

# Calculating and displaying total marks with grade
totalinfo.Grade()

#printing the skills involved in this course
print(totalinfo.course_skill(skills))
