class Person:
    def __init__(self, name, age):   # FIXED
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary
    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department
    def display(self):
        super().display()
        print(f"Department: {self.department}")

persons = []
employees = []
managers = []

def show_menu():
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Search Employee by ID")
    print("6. Exit")

def get_int_input(prompt):
    while True:
        value = input(prompt)
        if value.startswith('-') and value[1:].isdigit():
            return int(value)
        elif value.isdigit():
            return int(value)
        else:
            print("Invalid input! Please enter a number.")

def create_person():
    name = input("Enter Name: ")
    age = get_int_input("Enter Age: ")
    person = Person(name, age)
    persons.append(person)
    print(f"Person created: {name}, Age: {age}")

def create_employee():
    name = input("Enter Name: ")
    age = get_int_input("Enter Age: ")
    emp_id = input("Enter Employee ID: ")
    salary = float(get_int_input("Enter Salary: "))
    employee = Employee(name, age, emp_id, salary)
    employees.append(employee)
    print(f"Employee created: {name}, ID: {emp_id}")

def create_manager():
    name = input("Enter Name: ")
    age = get_int_input("Enter Age: ")
    emp_id = input("Enter Employee ID: ")
    salary = float(get_int_input("Enter Salary: "))
    department = input("Enter Department: ")
    manager = Manager(name, age, emp_id, salary, department)
    managers.append(manager)
    print(f"Manager created: {name}, Department: {department}")

def show_details():
    print("\nChoose details to show:")
    print("1. Persons")
    print("2. Employees")
    print("3. Managers")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not persons:
            print("No persons found.")
        for p in persons:
            print("\nPerson Details:")
            p.display()

    elif choice == "2":
        if not employees:
            print("No employees found.")
        for e in employees:
            print("\nEmployee Details:")
            e.display()

    elif choice == "3":
        if not managers:
            print("No managers found.")
        for m in managers:
            print("\nManager Details:")
            m.display()

    else:
        print("Invalid choice!")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")

    for e in employees:
        if e.emp_id == emp_id:
            print("\nEmployee Found:")
            e.display()
            return

    for m in managers:
        if m.emp_id == emp_id:
            print("\nManager Found:")
            m.display()
            return

    print("Employee not found.")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        create_person()
    elif choice == "2":
        create_employee()
    elif choice == "3":
        create_manager()
    elif choice == "4":
        show_details()
    elif choice == "5":
        search_employee()
    elif choice == "6":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")