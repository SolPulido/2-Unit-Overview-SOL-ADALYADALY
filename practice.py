name = input("What's your name? ")
print("Hey there! "+ name + ", Let's do something FUN")
#What are the arithmetic operators? 
#exponents operator: **
#multiplication operator: *
#divition operator: / 
#assigment operator: = 
#Addition operator: + 
#remainer operator:  %
#substraction operator: - 
#intergral divition operator : //
num1=int(input("Enter a number here : "))
num2=int(input("Enter amother number here : "))
print(" ")
#print(num1 + num2)  you are the only one that can see not the user 
sum = num1 + num2 # Addition operator 
multi = num1 * num2# multiplication operator 
divi = num1 / num2 # division operator
subs = num1 - num2 #substraction operator 
remain = num1 % num2 #remainer operator 
integral = num1 // num2 #integral operator (calclate whole number)
exponents = num1 ** num2 #calculate num1 to the power of num2 
print("The sum of your 2 numbers is : " + str(sum) )
print("The multiplication of your 2 numbers is : " + str(multi))
print("The divison of your 2 numbers is: " + str(divi))
print("The substraction of your 2 numbers is : " + str(subs))
print("The remain of your 2 numbers is : "+ str(remain))
print("The integral divition of your 2 numbers is : " + str(integral))
print("The exoponents of your 2 number is : " + str(exponents))