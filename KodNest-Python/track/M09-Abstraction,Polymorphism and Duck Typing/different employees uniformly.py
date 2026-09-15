class PermanentEmployee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"{self.name} - Permanent - Salary: {self.salary}"

class TemporaryEmployee:
    def __init__(self,name,contract_months):
        self.name = name
        self.contract_months = contract_months

    def show_details(self):
        return f"{self.name} - Contract - Duration: {self.contract_months}"

permanent_name = input().strip()
salary = int(input())
contract_name = input().strip()
contract_months = int(input())

permanent_employee = PermanentEmployee(permanent_name,salary)
contract_employee = TemporaryEmployee(contract_name,contract_months)

employees = [permanent_employee,contract_employee]

for employee in employees:
    print(employee.show_details())

#summary : here i created two classes permanent employee and temporary employee and i created show_details method in both classes and i used it to display the details of permanent employee and temporary employee