from abc import ABC, abstractmethod


class Human(ABC):
    @abstractmethod
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if len(first_name) < 4:
            raise Exception("Expected length at least 4 symbols! Argument: firstName")
        elif not first_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: firstName")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if len(last_name) < 3:
            raise Exception("Expected length at least 3 symbols! Argument: lastName")
        elif not last_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: lastName")
        self._last_name = last_name

    @abstractmethod
    def __str__(self):
        pass


class Student(Human):
    def __init__(self, f_n, l_n, id_number: int): #sorry, got lazy with the long var names
        super().__init__(f_n, l_n)
        self.id_number = id_number

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        if not 5 <= len(id_number) <= 10 or not id_number.isalnum():
            raise Exception("Invalid faculty number!")
        self._id_number = id_number

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nFaculty number: {self.id_number}"


class Worker(Human):
    def __init__(self, f_n, l_n, weekly_salary, work_hrs):
        super().__init__(f_n, l_n)
        self.weekly_salary = float(weekly_salary)
        self.work_hrs = float(work_hrs)

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, weekly_salary):
        if weekly_salary < 10:
            raise Exception("Expected value mismatch! Argument: weekSalary")
        self._weekly_salary = weekly_salary

    @property
    def work_hrs(self):
        return self._work_hrs

    @work_hrs.setter
    def work_hrs(self, wrk_hr):
        if not 1 <= wrk_hr <= 12:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")
        self._work_hrs = wrk_hr

    def calc_hourly_wage(self):#workdays 5 per week
        return self.weekly_salary/self.work_hrs/5

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nWeek Salary: {self.weekly_salary:.2f}\n" \
            f"Hours per day: {self.work_hrs:.2f}\nSalary per hour: {self.calc_hourly_wage():.2f}"


try:
    student = eval('Student')(*input().split())
    worker = eval('Worker')(*input().split())
    print(f"{student}\n")
    print(worker)
except Exception as e:
    print(e)
