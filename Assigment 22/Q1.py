import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("Employee ID:", self.eid)
        print("Employee Name:", self.ename)
        print("Basic Salary:", self.basic)

e1 = Emp(101, "Anjali", 25000)

with open("emp.dat", "wb") as f:
    pickle.dump(e1, f)

print("Object pickled successfully!\n")


with open("emp.dat", "rb") as f:
    emp_obj = pickle.load(f)

print("Object unpickled successfully!")
emp_obj.display()
