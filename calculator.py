a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
print("add / sub / mul / div")
c=str(input("Enter any one operation:"))
if c=="add":
  print("Add:",a+b)
elif c=="sub":
   print("Sub:",a-b)
elif c=="mul":
   print("Mul:",a*b)
elif c=="div":
  print("div:",a/b)
else:
   print("Invalid Input")
