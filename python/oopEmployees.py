class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + '.' + last + '@company.com').lower()
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Andrei', 'Briceag', 50000)
emp_2 = Employee('Test', 'Name', 45000)



print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_1.pay)