from functools import wraps

def my_deco(func):

    @wraps(func)
    def wr():
        print("Before")
        func()
        print("After")
    return wr

@my_deco
def greet():
    print("My first decorator")

greet()
print(greet.__name__)