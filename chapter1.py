## immutable
sugar = 2
print(f"Sugar1 = {sugar}")

sugar = 12
print(f"Sugar2 = {sugar}")


print(f"ID of 2 = {id(2)}")
print(f"ID of 12 = {id(12)}")



##mutable
spice_mix = set()
print(spice_mix)
print(f"ID of spice = {id(spice_mix)}")

spice_mix.add("s")
spice_mix.add("a")
spice_mix.add("t")
print(spice_mix)
print(f"ID of spice = {id(spice_mix)}")
