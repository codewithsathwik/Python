#method resolution order

class A:
    label = "A : Base class"
    
class B(A):
    label = "b : masala"

class C(A):
    label = "c : herbal"

class D(C, B):
    pass

cup = D()
print(cup.label) # here c is printed as it is inhertited first
print(D.__mro__)
