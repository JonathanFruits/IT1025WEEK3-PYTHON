num1=5
num2=2

print(num1 , num2)

sum=num1 + num2

print("sum=",sum)

diff=num1- num2

print("diff=",diff)

prod = num1 * num2
print("prod=",prod)
quotient= num1/num2
print("quotient=",quotient)
remainder= num1 % num2
print("remainder=", remainder)
age = input("Enter your age ")
if (int(age) <18 ):
  print("You cannot vote yet!")
else:
  print("Please vote!")

km = input("Enter how many kilometers you drove ")
miles = float(km) * 0.62
print("You drove", miles , " miles")