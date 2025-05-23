class Employee:
    def __init__(self, emp_id, name, dept, address, join_date):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.address = address
        self.join_date = join_date

employees = []
for i in range(5):
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    address = input("Enter Address: ")
    join_date = input("Enter Joining Date: ")
    employees.append(Employee(emp_id, name, dept, address, join_date))

search_dept = input("Enter department to search: ")

for emp in employees:
    if emp.dept == search_dept:
        print("\nEmployee Details:")
        print("ID:", emp.emp_id)
        print("Name:", emp.name)
        print("Address:", emp.address)
        print("Joining Date:", emp.join_date)
