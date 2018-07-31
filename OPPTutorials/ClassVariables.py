"""
Class Variables = Variables that is shared with all particles(instances) of that class
Instance variables could be unique for each instances (particle ) of a class , example person A might have a unique/different First and last name compared to person B

Class Variables are same for all instances

Purpose of this code is to show the purpose of Instance variables and class variables and when to use each style of variable .

NextCode: Will display class methods , static methods. Just like how there is class variables and instance variables, there also exists class methods and static methods

"""


# Building our class
class Employee:
    # Building a class variable
    raise_amount = 1.04
    num_of_emp = 0

    # Building/initializing the constructor of the class , this will be used to take in new instances
    def __init__(self, first_name, last_name, annual_income):
        self.firstName = first_name
        self.lastName = last_name
        self.annualIncome = annual_income
        # We keep track of the number of employees here because the init method is what's responsible for running every time we create a new employee
        Employee.num_of_emp += 1
        # The reason we use Employee.num_of_emp instead of self.num_of_emp because we want this variable to be constant throughout the entire class and can only be overridden (changed) when a new instance appears. Also there is no  practical reason to have different number of employees for each instance of Employee

    # Building method to return the employee's Annual income
    def give_annul_income(self):
        return "{}".format(self.annualIncome)

    # Building the full name method of each instance/particle of the Employee Class
    def full_employee_name(self):
        return "{} {}".format(self.firstName, self.lastName)

    # Hard Coding class variable
    def apply_raise(self):
        # If we use the  class variable raise_amount as is , then we will get a NameError BECAUSE !!: If we want to access the class variables we need to either 1) access them through class  itself ie. Employee.raise_amount
        # 2) We can access the class  variable through the instance of the class ie. self.raise_amount **THIS IS GOOD BECAUSE** It allows us to chnage the variable class for a single instance variable
        # **Also , using .self will low any subclass override the that constant if they want to
        self.annualIncome = int(self.annualIncome * self.raise_amount)


print("You currently have :", Employee.num_of_emp,
      "Employees")  # output is 0 , because we don'thave any new instances in our class

# Creating our instance object and passing in the instance variables
employee1 = Employee("Fname1", "Lname1", 5000)
employee2 = Employee("Fname2", "Lname2", 60000)

# Printing out the applyRaise Method for each instances variable
print("----------------")
print("\tEmployee1")
print("Before Raise: $", employee1.give_annul_income())
print("After the Raise:",
      employee1.apply_raise())  # This returns None, because we're only calling this method on our instance in order to apply the raise to their income and we are NOT returning anything , we're just modifying a variable of our instance particle
# Now we return the annual Income of our instance (particle) once applied the raise
print("After the Raise:$" + str(employee1.annualIncome))

print("----------------")
print("\tEmployee2")
print("Before Raise:$", employee2.give_annul_income())
print("After the Raise:",
      employee2.apply_raise())  # This returns None since we're not returning anything and instead modifying the variable of our instance particle
# Checking/Accessing the Employee 2 annual Income after applying the Raise
print("After the Raise:$" + str(employee2.annualIncome))

# Qsn If we have a class variable then why can we access them from our instance
print("----------------")
Employee.raise_amount = 1.05  # This changes all the raise amount of the class and the instance variable
print(Employee.raise_amount)  # output 1.05
print(employee1.raise_amount)  # output 1.05
print(employee2.raise_amount)  # output 1.05

print("-------Changing just the Instance variable raise amount--------")
employee2.raise_amount = 5  # This changes all the raise amount of the class and the instance variable
print(Employee.raise_amount)  # output 1.05
print(employee1.raise_amount)  # output 1.05
print(employee2.raise_amount)  # output 5 , only change.

# Qsn from above output, why is employee2 have a different output compares to Employee and employee1?
# Ans= When we made this assignment "employee2.raise_amount=5" we basically created the raise amount attribute (element) for the employee 1 ( basically it has it's own value and it doesn't need to worry about what value everyone else has)


# print("----------------")
# # Getting access to the name spaces for the instance variable
# print(employee1.__dict__)
# print(employee2.__dict__)

# Getting the namespaces for the Employee Class so see the values they can return
# print(Employee.__dict__)


# Getting the Number of current employees
print("----------------")
# Format className.attribute you want to use , example Employee.num_of_emp
print("You currently have :", Employee.num_of_emp, "Employees")
