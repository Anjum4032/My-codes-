# Calculate the sum of numbers until user enters 0
number = int(input('Enter a number: '))
total = 0
Operator = "+"
# iterate until the user enters =
while Operator != "=":
    Operator = input("Enter Opearator : ")
    if Operator == "+":
     total += number
     number = int(input('Enter a number: '))
     Operator2 = "+"
    elif Operator == "-":
     number = int(input('Enter a number: '))
     total -= number
     Operator2 = "-"
    elif Operator == "*":
     total *= number
    elif Operator == "/":
     total /= number
    #elif Operator == "=":
     #print (" ")
    else:
     print("Error")
if Operator2 == "+":
    total += number
elif Operator2 == "-":
    total -= number
print('The Answer is', total)