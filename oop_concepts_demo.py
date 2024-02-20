# Abstraction - keeping only required attributes and hiding complex/restricted details
# In python ,_denotes private and __protected; can be applied to attributes or methods
class Person:
    def __init__(self,name,gender,age,race,ethnicity):
        self.name = name
        self.gender = gender
        self.age = age
        self._race = race
        self._ethnicity = ethnicity
    def __str__(self):
        return f'Name:{self.name} Gender:{self.gender},Age:{self.age},Race:{self.race},Ethnicity:{self.ethnicity}'

per1 = Person('Jim','Male',28,'White','American')
print(per1)