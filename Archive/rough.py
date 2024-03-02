class HyrbidVehicle():

    def __init__(self,hv):
        self.hv='Hybrid Vehicle'
    
    def check_range(self):
        print('Available Range 200 miles')
class Toyota(HyrbidVehicle):

    def __init__(self,hv):
       self.name='Toyota Prius Prime'
       super().__init__(hv) # If parent class attribute

    def check_range(self): #overriding parent class method
        return 'Available Hybrid Range is 50 miles'


t=Toyota('Hybrid Vehicle')
print(t.name+':'+t.check_range())