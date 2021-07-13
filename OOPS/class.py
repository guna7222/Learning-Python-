# A class is like object constructor or a blueprint for creating objects
class Persion:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
ob1 = Persion('Gunasekhar', 23, 'Male')
print(ob1.name)
print(ob1.age)
print(ob1.gender)

    
