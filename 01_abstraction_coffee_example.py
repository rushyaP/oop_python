"""
The main intention of Abstraction is to hide complexity.
In coffee machine, to make coffee machine, user selects bean type, coffee and strength
The machine gives coffee

The same is implemented here. Coffee Machine class takes the input and gives coffee as result
Grinder, Brewer and Coffee class details are hidden within Coffee Machine class
"""

coffee_beans_map = {
    "Arabica": ["Espresso", "Americano", "Cappuccino", "Latte"],
    "Robusta": ["Espresso", "Ristretto", "Affogato"],
    "Liberica": ["Espresso", "Macchiato", "Flat White"],
    "Excelsa": ["Espresso", "Long Black", "Irish Coffee"],
    "Geisha": ["Espresso", "Pour Over", "Cold Brew"],
    "Maragogipe": ["Espresso", "Turkish Coffee", "Vietnamese Coffee"]
}

class Coffee:
    def __init__(self,input_bean,input_kind,input_strength):
        self.coffee_bean = input_bean
        self.coffee_kind = input_kind
        self.coffee_strength = input_strength

    def __str__(self):
        return f'{self.coffee_bean} {self.coffee_kind} {self.coffee_strength} is ready'
    
class CoffeeGrinder:
    def __init__(self,name):
        self.beanName = name
    def grind(self):
        if self.beanName in (coffee_beans_map.keys()):
            print('Grinding {x} beans...'.format(x=self.beanName))
            return f'{self.beanName}'
        else:
            print('{x} not available'.format(x=self.beanName))
            return None
        
class CoffeeBrewer:
    def __init__(self,bean,kind):
        self.coffeebean = bean
        self.coffeekind = kind
    def brew(self):
        if self.coffeebean not in coffee_beans_map.keys():
            print('Please select in the available bean types')
            return None
        elif self.coffeekind in coffee_beans_map[self.coffeebean]:
            print('Brewing {x}...'.format(x=self.coffeekind))
            return f'Brewing {self.coffeekind}'
        else:
            print('Please select another combination')
            return None
        
class CoffeeMachine:
    #Available strenghts - Light, Medium Strong
    def __init__(self,input_bean, input_kind,input_strength):
        self.selected_bean = input_bean
        self.selected_kind = input_kind
        self.selected_strength = input_strength
    def make_coffee(self):
        grindObj = CoffeeGrinder(self.selected_bean)
        brewObj = CoffeeBrewer(self.selected_bean,self.selected_kind)
        if grindObj.grind() is not None and brewObj.brew() is not None:
            coffeeObj = Coffee(self.selected_bean,self.selected_kind,self.selected_strength)
            print(coffeeObj)
cmObj = CoffeeMachine('Excelsa','Espresso','Light')
cmObj.make_coffee()   

#Output
"""  
Grinding Excelsa beans...
Brewing Espresso...
Excelsa Espresso Light is ready
"""

cmObj2 = CoffeeMachine('Excela','Espresso','Light')
cmObj2.make_coffee() 
#Ouput2
"""
Excela not available
"""

cmObj3 = CoffeeMachine('Excelsa','Esprsso','Light')
cmObj3.make_coffee() 
#Output3 --work on better output
"""
Grinding Excelsa beans...
Please select another combination
"""

