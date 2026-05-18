class BaseChai:
    def __init__(self,ty):
        self.ty = ty

    def prepare(self):
        print(f"Preparing : {self.ty} ")


class MasalChai(BaseChai):
    def addSpices(self):
        print("Adding cardemomo, ginger.......")


class ChaiShop:
    chai_cl = BaseChai
    def __init__(self):
        self.chai = self.chai_cl("Regular")

    def serve(self):
        print(f"Serving {self.chai.ty}")
        self.chai.prepare()

class Fancy(ChaiShop):
    # here chaishop constructor is
    chai_cl = MasalChai
    

shop = ChaiShop()
fnacy = Fancy()
shop.serve()
fnacy.serve()
# fnacy.chai.prepare()
fnacy.chai.addSpices()