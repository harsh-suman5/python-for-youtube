# The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow. For example:
#defing more than one arguments in function

# def sum(a, b= 7):
#     c = a+b
#     return c
# print(sum(3))
def list(a, list = []):
    list.append(a)
    return list
print(list(1))
print(list(2))
print(list(3))