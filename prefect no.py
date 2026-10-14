n=int(input("Enter the Number:"))
sum=0
for i in range(1,n):
  if n%i==0:
    sum+=i
if sum==n and n>0:
  print("Prefect Number")
else:
  print("Not Prefect Number")