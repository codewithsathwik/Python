def serve_chai():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = serve_chai()

print(next(chai))
print(next(chai))
print(next(chai))


#infinite generator
def infinte_gen():
    count = 1
    while(True):
        yield f"Recall {count}"
        count += 1


count_gen = infinte_gen()

for i in range(5):
    print(next(count_gen))


#send data to generators
def chai_customers():
    print("Welcome!")
    order = yield
    while(True):
        print(f"Preparing : {order}")
        order = yield

stall = chai_customers()
next(stall)

stall.send("Masala chai")
stall.send("Lemon chai")


#close generator
def india_menu():
    yield "Masala"
    yield "Ginger"

def imported_chai():
    yield "Oolong"
    yield "Maatcha"


def full_menu():
    yield from india_menu()
    yield from imported_chai()

for chai in full_menu():
    print(chai)




# close generator
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai"
    except:
        print("Stall is closed")

stall = chai_stall()
print(next(stall))
print(next(stall))
stall.close()