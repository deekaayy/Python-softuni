class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def age(self):
        return self.age
    
    @age.setter
    def age(self, value):
        if age < 0:
            raise Exception("Age must be positive!")
        self._age = age

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        self._name = name

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    @property
    def age(self):
        return self.age
    
    @age.setter
    def age(self, value):
        if age > 15:
            raise Exception("Child's age must be less than 15!")
        self._age = age


name = input()
age = int(input())
try:
    child = Child(name, age)
    print(child)
except Exception as e:
    print(e)