class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

def sort_employees(employees, sort_param):
    if sort_param == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_param == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_param == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return employees

def main():
    employee_data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000)
    ]

    employees = [Employee(*data) for data in employee_data]

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sort_param = int(input())

    sorted_employees = sort_employees(employees, sort_param)
    
    print("Sorted Employee Data:")
    for emp in sorted_employees:
        print(emp)

if __name__ == "__main__":
    main()
