n=int(input("Enter the Number:"))
m=len(str(n))
au=n*n
au=str(au)
last=int(au[-m:])
if last==n:
  print("Automrophic")
else:
  print("Not Automrophic")