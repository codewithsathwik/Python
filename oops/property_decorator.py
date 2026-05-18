class Chai:

    def __init__(self,age):
        #anything in python like _age, _ty is said to have getter and setter
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("age is not proper")
        

leaf = Chai(2)
print(leaf.age)