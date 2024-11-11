# Basic Calculator

def add(x, y):
    return x + y

def multiplaction(x, y):
    return x * y

def subtraction(x, y):
    return x - y

def division(x, y):
    return x / y

num1 = float(input ("first number "))
num2 = float(input ("second number "))
print ("1 = add")
print ("2 = multiplaction")
print ("3 = subtraction")
print ("4 = division")
user = input ("which operation?
              1 or 2 or 3 or 4: ")

if user == "1":
    print (add(num1, num2))

elif user == "2":
    print (multiplaction(num1, num2))

elif user == "3":
    print (subtraction(num1, num2))

elif user == "4":
    print (division(num1, num2))

else:
    print ("Invalid operation")

