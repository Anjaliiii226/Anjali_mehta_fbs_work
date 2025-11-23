import pickle
import os

FILENAME = "employees.dat"


class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f"ID: {self.eid}, Name: {self.ename}, Salary: {self.basic}")


def load_data():
    """Load employee list from file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "rb") as f:
        return pickle.load(f)


def save_data(emp_list):
    """Save employee list to file."""
    with open(FILENAME, "wb") as f:
        pickle.dump(emp_list, f)


def add_record():
    emp_list = load_data()
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)
    emp_list.append(emp)
    save_data(emp_list)
    print("Record added successfully!\n")


def search_record():
    emp_list = load_data()
    eid = int(input("Enter ID to search: "))
    for emp in emp_list:
        if emp.eid == eid:
            print("Record found:")
            emp.display()
            return
    print("Record not found!\n")


def delete_record():
    emp_list = load_data()
    eid = int(input("Enter ID to delete: "))

    for emp in emp_list:
        if emp.eid == eid:
            emp_list.remove(emp)
            save_data(emp_list)
            print("Record deleted successfully!\n")
            return

    print("Record not found!\n")


def edit_record():
    emp_list = load_data()
    eid = int(input("Enter ID to edit: "))

    for emp in emp_list:
        if emp.eid == eid:
            print("Existing Record:")
            emp.display()

            # New values
            emp.ename = input("Enter new name: ")
            emp.basic = float(input("Enter new salary: "))

            save_data(emp_list)
            print("Record updated successfully!\n")
            return

    print("Record not found!\n")


def display_all():
    emp_list = load_data()
    if not emp_list:
        print("No records found!\n")
        return

    print("\nAll Employee Records:")
    for emp in emp_list:
        emp.display()
    print()


def main():
    while True:
        print("\n--- Employee File Management ---")
        print("1. Add Record")
        print("2. Search Record")
        print("3. Delete Record")
        print("4. Edit Record")
        print("5. Display All Records")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_record()
        elif choice == '2':
            search_record()
        elif choice == '3':
            delete_record()
        elif choice == '4':
            edit_record()
        elif choice == '5':
            display_all()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

main()
