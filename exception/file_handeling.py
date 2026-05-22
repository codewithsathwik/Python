#native method to open the file

# file = open("order.txt","w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()


#OR

#file.close() calls ->  file.__exit__(). and file.__enter__() as begining.
#the below method does it all automatically
#to open file we use different libraries, this is not right way

with open("order.txt", "w") as file:
    file.write("Ginger chai - 2 cups")