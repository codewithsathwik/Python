class Chaicup:
    size = 150

    def des(self):
        return (f"The size  is : {self.size}ml")


cup = Chaicup()
print(cup.des())
cup.size = 50
print(Chaicup.des(cup))

cup_two = Chaicup
cup_two.size = 500
print(Chaicup.des(cup_two))