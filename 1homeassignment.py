num1=int(input("enter 1st integer no."))
num2=int(input("enter 2nd integer no."))
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
number = 10

if num1 > num2:
 print(num1, "is greater than", num2)
 Percent = float(num2/num1)*100
 print(num2, "is", Percent, "of", num1)
else:
 print(num2, "is greater than", num1)
 Percent = float(num1/num2)*100
 print(num1, "is", Percent, "of", num2)
print("the Subtraction of",num1 ,"and",num2 ,"are", sub)
print("the adition of",num1 ,"and",num2 ,"are", sum)
print("the multipilication of",num1 ,"and",num2 ,"are", mul)