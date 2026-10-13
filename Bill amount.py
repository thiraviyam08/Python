bill=int(input("Enter the Amount:"))
if (bill>=2000):
  amount=(bill*10)/100
  discount=bill-amount
  print(discount)
else:
  print("The Bill Amount is Below 2000")
  