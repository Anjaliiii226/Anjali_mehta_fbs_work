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

class EnggStudent(Student):
    def __init__(self, student_id=None, name=None, age=None, percentage=None,
                 branch=None, internal_marks=None):
        # Call base class constructor
        super().__init__(student_id, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    def display(self):
        super().display()  # Display base class info
        print(f"Branch       : {self.Branch}")
        print(f"Internal Marks: {self.InternalMarks}")
        print(f"Updated Rank : {self.calculate_rank()}")

    def accept(self):
        super().accept()  # Accept base details
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def calculate_rank(self):
        total = self.Percentage * 0.8 + self.InternalMarks * 0.2
        if total >= 90:
            return "Distinction"
        elif total >= 75:
            return "First Class"
        elif total >= 60:
            return "Second Class"
        elif total >= 50:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"[EnggStudentId: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, "
                f"Branch: {self.Branch}, Percentage: {self.Percentage}%, "
                f"Internal Marks: {self.InternalMarks}, Rank: {self.calculate_rank()}]")
