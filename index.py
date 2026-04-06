
# Function defined to add two numbers x and y
def add(x,y):
    return x+y

#Function defined to multiply two numbers x and y
def multiplication(x,y):
    return x*y

#Function defined to substract two number x and y
def substraction(x,y):
    return x-y

#Function defined to find the value of x to the power of y
#Important: Y is the exponential power and x is the base value. It is of the form (x)^y
def exponents(x,y):
    return x**y

#Function defined to divide two numbers.
#The result is always going to be in decimal form.
def division(x,y):
    return x/y



x = int(input("Number 1: "))
y = int(input("Number 2:- "))

#Calls the "Add" function
#When a function is called the result is stored in the calling function.
add(x,y)

#Prints the result of the "Add" function
print("The additon of the numbers x and y is" ,add(x,y))

#Prints the result of the multiplication function
print("The multiplication of the numbers X and Y is", multiplication(x,y))

#Prints the result of the substraction function
print("The subsctraction of the two numbers x and y is", substraction(x,y))

#Prints the result of the exponent function
# IMPORTANT: In the exponent function the value of exponent is "y" and the base value is "x"
print("The value of x to the power of y is ", exponents(x,y))

#Prints the result of the division function
#The output is always in decimal numbers.
print("The division of the two numbers x and y is",division(x,y))