menu = [
    "Msasla",
    "Iced coffee",
    "Ginger",
    "Iced tea"
]
# var = [expression for var in collection if condition]
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)


# var = {expression for var in collection if condition}
faverate_chai=[
    "Msasla",
    "Green tea",
    "Masala",
    "Iced tea",
    "Green tea"
]

unique_chai = {chai for chai in faverate_chai if len(faverate_chai) < 8}
print(unique_chai)

recipies = {
    "Masala" : ["ginger","cardamum"],
    "elaichi chai" : ["clove","Milk"],
    "Spicy" : ["ginger","clove","black pepper"],
}

unique_dict = {r for rec in  recipies.values() for r in rec}
print(unique_dict)

#dictonaries
prices = {
    "Masala" : 80,
    "elaichi chai" : 75,
    "Spicy" : 100,
}
tea_price = {tea:price for tea,price in prices.items()}
print(tea_price)


#====================GENERATORS====================
#VAR = (expression for item in iterable)
daily_sales = [5,8,9,4,2,15,20]

# total_cups = (sale for sale in daily_sales if sale > 10)
total_cups = sum(sale for sale in daily_sales if sale > 10)
print(total_cups)