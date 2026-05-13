# scope

# chai = "Tea"

# def sample_function():
#     global chai
#     chai = "function"
#     print(chai)

# sample_function()
# print(chai)


# chai = "global"
# def print_chai():
#     chai = "irani"
#     def sample():
#         nonlocal chai
#         chai = "local"
#         print(chai)
#     sample()
#     print(chai)

# print_chai()
# print(chai)

#arguments
# def function_arguments(*tup, **di):
#     print(f"Args : {tup}") 
#     print(f"Key  : {di}")

# function_arguments("chai","tea","coffee",sugar="sweet",salt="biter")



#documentaion

def chai_type(flavor="Chai"):
    """Return the chai falvour."""
    chai="Ginger"
    return flavor

print(chai_type())
print(chai_type.__name__)
print(chai_type.__doc__)

help(len)