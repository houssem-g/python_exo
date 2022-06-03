class Employee:
    def __init__(self, firstName, lastName, salary):
        self.firstname = firstName
        self.lastname = lastName
        self.salary = salary
    @classmethod
    def from_string(cls, completeStr):
        mySplit = completeStr.split(sep='-')
        firstname = mySplit[0]
        lastname = mySplit[1]
        salary = int(mySplit[2]) 
        return cls(firstname, lastname, salary)
        
         
        

emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp2.firstname)
