n=int(input("Enter a number:"))
if n%1==0 and n%n==0:
  if n%2!=0 or n==2:
    print("The given number is prime number")
  else:
      print("The given number is not a prime number")