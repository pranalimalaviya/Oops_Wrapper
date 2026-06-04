# Employee Management System (Python OOP)

A simple **Employee Management System** built using **Python Object-Oriented Programming (OOP)** concepts. This project demonstrates **Inheritance**, **Method Overriding**, **Encapsulation**, and basic **CRUD-style operations** through a command-line interface.

## Features

* Create and manage **Persons**
* Create and manage **Employees**
* Create and manage **Managers**
* Display stored records
* Search employees by Employee ID
* Input validation for numeric values
* Demonstrates multi-level inheritance

## OOP Concepts Used

### 1. Inheritance

The project uses inheritance to extend functionality:

Person
   ↓
Employee
   ↓
Manager

### 2. Method Overriding

Each child class overrides the `display()` method to include additional information.

### 3. Constructor Chaining

super() is used to call parent class constructors.

### 4. Encapsulation

Attributes are stored inside objects and managed through class methods.

## Project Structure

text
Oops_Wrapper.py
│
├── Person Class
├── Employee Class
├── Manager Class
│
├── Create Person
├── Create Employee
├── Create Manager
│
├── Show Details
├── Search Employee By ID
└── Menu Driven Interface

## Classes

### Person

Attributes:

* Name
* Age

Methods:

* `display()`

### Employee

Inherits from `Person`

Additional Attributes:

* Employee ID
* Salary

Methods:

* `display()` (overridden)

### Manager

Inherits from `Employee`

Additional Attributes:

* Department

Methods:

* `display()` (overridden)

## Menu Options
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Search Employee by ID
6. Exit

## Example Output
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Search Employee by ID
6. Exit

Enter your choice: 2
Enter Name: John
Enter Age: 25
Enter Employee ID: EMP101
Enter Salary: 50000

Employee created: John, ID: EMP101

## How to Run

### Prerequisites

* Python 3.x installed

### Run the Program

bash
python Oops_Wrapper.py

## Learning Objectives

This project is useful for beginners learning:

* Python Classes and Objects
* Inheritance
* Method Overriding
* Constructor Chaining (`super()`)
* Menu-Driven Programs
* Data Management using Lists

## Future Improvements

* Store data in files or databases
* Add update and delete operations
* Improve input validation
* Implement exception handling
* Add a graphical user interface (GUI)
* Export employee records to CSV/Excel

## Author

Created as a Python OOP practice project to demonstrate inheritance and object-oriented programming concepts.
