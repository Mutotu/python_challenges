print("Welcome to Chase bank.")
print("Have a nice day!")


def main():

  balance = 0
  request = input("What would you like to do? (1:deposit, 2:withdraw, 3:check balance, q:to quit => ")
  while  request in ["1","2","3"]:
    if request == "1":
      deposit = int(input("How much would you like to deposit?: "))
      balance += deposit
    elif request == "2":
      withdraw = int(input("How much would you like to withdraw?: "))
      if withdraw > balance:
        print("Your balance is less than that.")
        print("Your current balance is ", balance)
        withdraw = int(input("How much would you like to withdraw?: "))
        balance -= withdraw
    elif request == "3":
      print("Your current balance is ", balance)
    print("Your current balance is ", balance)
    request = input("What would you like to do? (1:deposit, 2:withdraw, 3:check balance => ")

main()
