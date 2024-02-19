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
    
    def update_age(self,i):
        self.age += i

    def setCountry(self,country):
        self.country = country
    def getCountry(self):
        print(self.country)

    def display(self):
	    print("Person name is {name}. Age is {age}. Country is {country}".format(name=self.name,
         age=self.age,country=self.country))

person1 = Person('Ruby',25,'India')
person1.display()
print("updating")
person1.update_age(0.6)
person1.setCountry('USA')
person1.getCountry()
person1.display()

