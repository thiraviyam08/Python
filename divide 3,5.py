num=int(input("Enter the number:"))
if num%5==0 and num%3==0:
  print("The given number is divisible by 3,5")
elif num%5==0:
  print("The given number is divisible by 5")
elif num%3==0:
  print("The given number is divisible by 3")
else:
  print("The given number is not divisible by 3,5")