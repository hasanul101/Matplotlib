class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
     raise_amount = 1.10

     def __init__(self, first, last, pay, prg_lang):
        super().__init__(first, last, pay)
        self.prg_lang = prg_lang


dev_1 = Developer("Hasanul", "Raffi", 50000, 'R')
dev_2 = Developer("Rafael", "Dsouza", 30000, 'Python')

print(dev_1.email)
print(dev_2.prg_lang)














