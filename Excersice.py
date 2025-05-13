# print("hello world")
# hkjsedkhh
# Name = "Ghazale will be successful"
# print(len(Name))
# if "Go" not in Name:
#     print("yes")
# print(Name.count("  "))
# print(Name.index([0:]))
# -------------------------------------------------------
# First_number = int(input("Insert a number between 1 to 9: "))
# number = First_number

# number *= 2
# number += 8
# number += First_number
# number -= 2
# number /= 3
# number -= First_number
# number *= 4

# print(number)
# --------------------------------------------------------
# myList = ['red pride', 'blue dena', 'white BMW', 'red BMW', 'black Mercedes', 'yellow pars', 'red corvet']
# newList = [redCar for redCar in myList if "red" in redCar]

# print(newList)
# --------------------------------------------------------
# print("Number Pattern ")

# row = 5

# for i in range(1, row + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")
# --------------------------------------------------------
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)
# --------------------------------------------------------
# def my_function(x):
#   return print(5 * x)


# my_function(int(input("Say a number: ")))
# --------------------------------------------------------
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

print(my_function(1))
print(my_function(3))
print(my_function(c = 2))
print(my_function(2))


