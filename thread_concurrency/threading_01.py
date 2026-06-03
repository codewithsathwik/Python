import threading
import time

def take_order():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)

# creating thread
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

#invoke or start thread
order_thread.start()
brew_thread.start()

#waiting for both to finish
order_thread.join()
brew_thread.join()

print(f"all the orders and brewing are done")