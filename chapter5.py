#strings

chai_type = "ginger chai"

customer = "Priya"

print(f"Order for {customer} : {chai_type} please !")

chai_des = "Aromatic and bold"
print(f"First word {chai_des[:8:1]}")
print(f"Last word {chai_des[12:]}")

print(f"Last word {chai_des[::-1]}") #shorthand for reversing the string

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(f"encoded word {encoded_label}")
print(f"non encoded word {label_text}")

decode = encoded_label.decode("utf-8")
print(f"Decoded word {decode}")