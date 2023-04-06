# String formating: Using placeholder for making concatination
#     %d digit
#     %s string
#     %f float

# name = "Islam Eltally"
# job = "DevopsEnginer"
# age = 32
# myBankAccount = 500623225311
# rank = 12

# print("My name is {:s} and I am working as {:.6s} , my age is {:d} and my Rank is {:.2f} and my account banking {:_d}" .format(
#      name, job, age, rank, myBankAccount))  # Modern Way
# print("My name is {:s} and I am working as {:.6s} , my age is {:d} and my Rank is {:.2f} and my account banking {:,d}" .format(
#     name, job, age, rank, myBankAccount))  # Modern Way


# print("My name is %s and I am working as %s , my age is %d and my Rank is %.2f" %
#       (name, job, age, rank))     #Old way

# print("My name is {:s} and I am working as {:.6s} , my age is {:d} and my Rank is {:.2f} and my account banking {:_d}" .format(
#     name, job, age, rank, myBankAccount))  # Modern Way
# print("My name is {:s} and I am working as {:.6s} , my age is {:d} and my Rank is {:.2f} and my account banking {:,d}" .format(
#     name, job, age, rank, myBankAccount))  # Modern Way
# Modern way = converted from old version %s to {} | {:s}  and from %d to {:d} and %f to {:f}
#   and the parameters from %(, , , ) to .format(, , ,)

x, y, z = "one", "two", "three"
a, b, c = 10, 20, 30
# print(x, y, z)
# print(a, b, c)
# print("The message to be printed  {1:s},{:2s},{0:s}".format(x, y, z))
# print("The message to be printed {1:d},{0:d},{2:d} ".format(a, b, c))
print(f"The message to be printed {x}, {y}, {z}")  # f ==> format operator
print(f"The message to be printed {a}, {c}, {b}")  # f ==> format operator

# http://pyformat.info/
