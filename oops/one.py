class Chai:
    pass


# print(type(Chai))




#namesapce

class ChaiTime:
    origin = "India"

ChaiTime.is_hot = False

print(ChaiTime.origin)
print(ChaiTime.is_hot)

masala = ChaiTime()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = True
print(ChaiTime.is_hot)
print(masala.is_hot)

#attribute shadowing