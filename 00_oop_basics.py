"""class Dog:
    def __init__(self, input_name,input_breed, input_age):
        self.name = input_name
        self.breed = input_breed
        self_age = input_age

dog_a = Dog('Arya','Husky',3)
print(dog_a.name)
"""

class Person:
    def __init__(self, input_name, input_age, input_country):
        self.name = input_name 
        self.age = input_age
        self.country = input_country

    #custom method
    def update_age(self,i):
        self.age += i

    #setters and getters
    def setCountry(self,country):
        self.country = country
    def getCountry(self):
        print(self.country)

    def display(self):
	    print("Person name is {name}. Age is {age}. Country is {country}".format(name=self.name,
         age=self.age,country=self.country))

    def __str__(self): # this gets called when an object of this class is printed
        return f'{self.name},{self.age},{self.country}'

    def __repr__(self): # this gets called when print of repr(object) is called
        return f'repr_method calling: {self.name},{self.age},{self.country}'

person1 = Person('Ruby',27,'India')
person1.display()
print("updating")
person1.update_age(0.6)
person1.setCountry('USA')
person1.getCountry()
person1.display()

#Output1
"""  
Person name is Ruby. Age is 27. Country is India
updating
USA
Person name is Ruby. Age is 27.6. Country is USA
"""

# The __dict__ attribute is found in every python object. It stores all the attributes of a class
print(person1.__dict__)
print(person1)

#Output2
"""
{'name': 'Ruby', 'age': 27.6, 'country': 'USA'}
Ruby,27.6,USA
"""

print(repr(person1))

#Output3
"""
repr_method calling: Ruby,27.6,USA
"""