class Employee:
    company_name = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # 1. Class Method (Alternative Constructor)
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, float(salary))

    # 2. Static Method (Utility)
    @staticmethod
    def is_work_day(day):
        return day.lower() not in ["saturday", "sunday"]

    # 3. Property (Getter)
    @property
    def salary(self):
        return self._salary

emp = Employee.from_string("Sarah-75000")
print(emp.salary)                   # Output: 75000.0 (Accessed like an attribute)
print(Employee.is_work_day("Monday")) # Output: True