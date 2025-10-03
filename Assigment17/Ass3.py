class Student:
    def __init__(self, student_id=None, name=None, age=None, percentage=None):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def display(self):
        print(f"Student ID   : {self.StudentId}")
        print(f"Name         : {self.Name}")
        print(f"Age          : {self.Age}")
        print(f"Percentage   : {self.Percentage}%")
        print(f"Rank         : {self.calculate_rank()}")

    def accept(self):
        self.StudentId = input("Enter Student ID: ")
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def calculate_rank(self):
        if self.Percentage >= 90:
            return "A+"
        elif self.Percentage >= 75:
            return "A"
        elif self.Percentage >= 60:
            return "B"
        elif self.Percentage >= 50:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return (f"[StudentId: {self.StudentId}, Name: {self.Name}, "
                f"Age: {self.Age}, Percentage: {self.Percentage}%, "
                f"Rank: {self.calculate_rank()}]")


# Derived Class - MedicalStudent
class MedicalStudent(Student):
    def __init__(self, student_id=None, name=None, age=None, percentage=None,
                 specialization=None, marks_of_internship=None):
        # Call base class constructor
        super().__init__(student_id, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marks_of_internship

    def display(self):
        super().display()  # Display base class info
        print(f"Specialization    : {self.Specialization}")
        print(f"Internship Marks  : {self.MarksOfInternship}")
        print(f"Updated Rank      : {self.calculate_rank()}")

    def accept(self):
        super().accept()  # Accept base details
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Marks of Internship: "))

    def calculate_rank(self):
        # Override: Use both percentage + internship marks (weighted)
        total = self.Percentage * 0.7 + self.MarksOfInternship * 0.3
        if total >= 90:
            return "Excellent Doctor"
        elif total >= 75:
            return "Very Good"
        elif total >= 60:
            return "Good"
        elif total >= 50:
            return "Average"
        else:
            return "Needs Improvement"

    def __str__(self):
        return (f"[MedicalStudentId: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, "
                f"Specialization: {self.Specialization}, Percentage: {self.Percentage}%, "
                f"Internship Marks: {self.MarksOfInternship}, Rank: {self.calculate_rank()}]")
