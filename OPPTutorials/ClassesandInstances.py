# In this file we will Explain How to create a simple class , the difference between a class and an instance of that class, and how to initialize class attributes and build our methods

class Employee:

    # creating the constructor/ initializer
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        # printing employee fullName

    def fullname(self):
        return "{} {}".format(self.first, self.last)


employee1 = Employee("Sam", "A", 50000)
employee2 = Employee("NyLa", "D", 6000000)

# prinitng the email of each instance
print(employee1.email)
print(employee2.email)

# print(employee1.fullname())

print("Employee 1 First Name is: ", employee1.fullname(), " Their Income is:$", employee1.pay)
print("Employee 2 Full Name is: ", employee2.fullname(), "There Income is:$", employee2.pay)

# The following block of code below , all do the same task just in a different way

# 0.Calling the method on the class but we need to pass in our instances because if we don't then the method will not take any arguments

    # Employee.fullname())  # This will result in an TypeError , because he haven't passed any arguments(instance variable) to the method of the class

    # Solution to fix the above error is to pass in the instance variable (Self) to the method of the class

print(Employee.fullname(employee1))
print(Employee.fullname(employee2))

# 1. Calling the method by using just our instances  (unit/item of a class)
# format is : instance.methodName()
employee1.fullname()
employee2.fullname()
