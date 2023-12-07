"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, bonus_commission=0):
        self.bonus_commission = bonus_commission

    def get_pay(self):
        pass

    def __str__(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus_commission=0, num_contracts=0, commission_per_contract=0):
        super().__init__(bonus_commission)
        self.name = name
        self.monthly_salary = monthly_salary
        self.bonus_commission = bonus_commission
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        contract_commission = self.num_contracts * self.commission_per_contract
        total_pay = self.monthly_salary + self.bonus_commission + contract_commission
        return total_pay

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}.  Their total pay is {self.get_pay}."



class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked, bonus_commission=0, num_contracts=0, commission_per_contract=0):
        super().__init__(bonus_commission)
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        contract_commission = self.num_contracts * self.commission_per_contract
        contract_pay = self.hourly_rate * self.hours_worked
        total_pay = contract_pay + self.bonus_commission + contract_commission
        return total_pay

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour " \
               f"and receives a bonus commission of {self.bonus_commission}. " \
               f"They have {self.num_contracts} contract(s) with a commission of {self.commission_per_contract}/contract. " \
               f"Their total pay is {self.get_pay()}."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, num_contracts = 4, commission_per_contract = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 25, 150, num_contracts = 3, commission_per_contract = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, bonus_commission = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 30, 120, bonus_commission = 600)
