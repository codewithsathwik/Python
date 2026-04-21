#boolean

boiling = True
count = 3
total = count + boiling #upcasting
print(f"Toal milk = {total}")

milk_present  = 1 # 0, None = false , >1 = true
# bool methods converts using the above condition
print(f"Is milk = {bool(milk_present)}") 


#logical operations
#and, or , not

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can i serve? = {can_serve}")