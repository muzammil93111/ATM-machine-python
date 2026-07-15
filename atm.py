pin = int(input("atm pin: "))
balance = 10000

if pin == 1122:
  while True:
    print( "1 check balance")
    print( "2 deposit")
    print( "3 withdraw")
    print( "4 exit")

    option=int(input("chose option: "))
    if option == 1:
      print("balance is: ",balance)

    elif option == 2:
      amount = int(input("enter amount: "))
      balance += amount
      print("balance is: ",balance)

    elif option == 3:
        amount = int(input("enter amount: "))
        if amount > balance:
          print("insufficient balance")
        else:
          balance -= amount
          print("balance is: ",balance)

    else:
      print("exit")
      break
 
else:
  print("invalid pin")
