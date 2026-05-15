# this is a  python script for a simple calculator

num1 = int(input("Enter First number: "))
num2 =  int(input("Enter second number: "))

operator = input ("Enter your operator (+, /, *, -): " )

if operator == '+':
  print("sum", num1+num2)
elif operator == '-':
  print("Difference = ", num1-num2)
elif operator == '*':
  print ("Product = ", num1*num2)
elif operator == '/':
  print ("division = ", num1/num2)
else:
  print("Invalid Operator")

