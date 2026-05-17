class Chai:
    temep = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temep)

cutting.temep = "Mild"
print(cutting.temep)
print(Chai.temep)

del cutting.temep
print(cutting.temep)


# cutting.cup = "small"

