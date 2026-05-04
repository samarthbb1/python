# 3a. Email Validation using RegEx

import re
def validate_email(email):
    pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    if re.match(pattern, email):
        print(f"{email} is Valid ")
    else:
        print(f"{email} is Invalid ")

validate_email("test@example.com")

# 3b. Salary Calculation using Class Methods
class Employee:
    base_pay = 50000  # Class variable

    @classmethod
    def calculate_salary(cls, bonus):
        return cls.base_pay + bonus

total = Employee.calculate_salary(5000)
print(f"Total Salary: ${total}")








