month=int(input("Enter the Month in number:"))
if month==2:
  print("The given month is february")
elif month in [4,6,9,11]:
  print("The given month is 30days")
elif month<=12:
  print("The given month is 31days")
else:
  print("Invalid Month")