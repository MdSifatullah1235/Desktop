lower = int(input("Enter a number for the lower range :"))
upper = int(input("Enter a number for the upper range :"))
print("The prime numbers between {} and {} are :".format(lower,upper))
for num in range(lower,upper + 1):
  if num > 1:
    for i in range(2,num):
     if num % i == 0:
       break
    else:
      print(num)