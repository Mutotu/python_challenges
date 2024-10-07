# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

def calculator():
  operaion = input("What calculation would you like to do? (add, sub, mult, div): ")
  num1 = int(input("What is number 1?: "))
  num2 = int(input("What is number 2?: "))
  if operaion == "add":
    return num1 + num2
  elif operaion == "sub":
    return num1 - num2
  elif operaion == "mult":
    return num1 * num2
  else:
    return num1 / num2

print(calculator())
print(calculator())
print(calculator())
print(calculator())
