class Employee:
    # A class representing an Employee
    EmployeeCount = 0   #Data member to count number of employees
    TotalSalary = 0
    def __init__(self,name,family,salary,dept): #Constructor to initialize
        self.EmpName = name
        self.EmpFamily = family
        self.EmpSalary = salary
        self.DeptName = dept
        Employee.TotalSalary = Employee.TotalSalary + self.EmpSalary
        Employee.EmployeeCount = Employee.EmployeeCount + 1
#Getters
    def getEmpName(self):
        return self.EmpName

    def getEmpFamily(self):
        return self.EmpFamily

    def getEmpSalary(self):
        return self.EmpSalary

    def getDeptName(self):
        return self.DeptName

    def getEmpCount(self):
        return Employee.EmployeeCount
#Function to calculate average salary based on employee count
    def calculateAvgSalary(self):
        avgSalary = Employee.TotalSalary // Employee.EmployeeCount
        return avgSalary

class FullTimeEmployees(Employee):  #Passing another class as parent
    # A class representing FullTime Employee and extending Employee
    def __init__(self,name,family,salary,dept,experience):
        Employee.__init__(self,name,family,salary,dept) #Call __init__ for Employee
        self.EmpExperience = experience #Constructor to initialize

        # Getters
    def getEmpExperience(self):
        return self.EmpExperience

emp = Employee('Manvi','IT',7000,'Banking') #Instance of Employee Class
#Print details of an employee
print("Name of Employee: ",emp.getEmpName())
print("Name of Employee's Family: ",emp.getEmpFamily())
print("Employee Salary: ",emp.getEmpSalary())
print("Department Name: ",emp.getDeptName())
print("Employee Count: ",emp.EmployeeCount)
print("Calculate Average Salary: ",emp.calculateAvgSalary())
print()

emp = Employee('Alex','IT',8000,'Developer') #Instance of Employee Class
#Print details of an employee
print("Name of Employee: ",emp.getEmpName())
print("Name of Employee's Family: ",emp.getEmpFamily())
print("Employee Salary: ",emp.getEmpSalary())
print("Department Name: ",emp.getDeptName())
print("Employee Count: ",emp.EmployeeCount)
print("Calculate Average Salary: ",emp.calculateAvgSalary())
print()

fullTimeEmp = FullTimeEmployees('Neela','Business',10000,'HumanResources','10Years') #Instance of Full Time Employees
#Print details of a full time employee
print("Name of FullTimeEmployee: ",fullTimeEmp.getEmpName())
print("Name of FullTimeEmployee's Family: ",fullTimeEmp.getEmpFamily())
print("FullTimeEmployee Salary: ",fullTimeEmp.getEmpSalary())
print("Department Name: ",fullTimeEmp.getDeptName())
print("FullTime Employee Experience: ",fullTimeEmp.getEmpExperience())
print("Employee Count: ",fullTimeEmp.EmployeeCount)
print("Calculate Average Salary: ",fullTimeEmp.calculateAvgSalary())