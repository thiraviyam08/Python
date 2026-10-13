mark=int(input("Enter the mark:"))
att=int(input("Enter the Attendence:"))
if mark>=90 and att>=85:
  print("The Student has get a scholarship")
elif mark<90 and att<85:
  print("The Student has not to get a scholarship")
elif mark>=90 or att>=85:
  print("The Student has not to get a scholarship")
else:
  print("Invalid value")