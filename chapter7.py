#mutable
#list -> []

ingred = ["water","air","milk"]
ingred.append("Ginger")
print(f"Ingredients : {ingred}")

chai_materilas = ["powder","cup"]
chai_materilas.extend(ingred)
print(f"Extended : {chai_materilas}")

#add at pos
chai_materilas.insert(2,"gun")
print(f"inserted : {chai_materilas}")

#remove
chai = ["water","hot","milk"]
removed = chai.pop()
print(removed)
chai.reverse()
chai.sort()
print(f"removed list : {chai}")

#max min
sugar = [1,2,3,4,5]
print(f"Max : {max(sugar)}")
print(f"Min : {min(sugar)}")