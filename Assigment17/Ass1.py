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
