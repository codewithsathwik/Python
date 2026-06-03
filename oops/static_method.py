class ChaiUtils:

    @staticmethod
    def clenaIng(text):
        return [item.strip() for item in text.split(",")]


st = " Water, ginger, milk"
chai = ChaiUtils.clenaIng(st)
print(chai)



#class method
class chaiOrder:
    def __init__(self,teatype, sweet, size):
        self.teatype = teatype
        self.sweet = sweet
        self.size = size
    
    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["teatype"],
            order_data["sweet"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls, order):
        teatype, sweet, size = order.split(",")
        return cls(teatype,sweet,size)

order1 = chaiOrder.from_dict(
    {
        "teatype" : "ginger",
        "sweet" : "low",
        "size" : "large" 
    }
)

order2 = chaiOrder.from_string("Ginger,low,small")

print(order1.__dict__)
print(order2.__dict__)
# print(order3.__dict__)

