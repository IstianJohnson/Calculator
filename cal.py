#It is a simple calculator for a user to do calculations easily it is a beginner level code to get hands on python 
#things to know about the code
# commands used in it are 
# def, print, if, elif and else

#defining the functions using def
def add(x, y):
    return x + y 

def subtract(x, y):
    return x - y 
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    if y == 0 :
        return "cannot divide with 0"
    return x / y
#It will be the front page    
print("Welcome to Fedis's Calculator")
print("For addition press 1")
print("For subtraction press 2")
print("For multiplication press 3")
print("For division press 4")

#it is a choosing machanism in which the person eill enter the opration
choose = (input("Enter the opration : "))

#Sending the first and the second digit it can more the two also according to the need of the developer using the same command and doing some slight changes
num1 = float(input("Enter First Digit : "))
num2 = float(input("Enter Second Digt : "))


#Its the main place where the opration will take place
if choose == '1':
    print(num1, "+", num2, "=", add(num1, num2))
    
elif choose == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
    
elif choose == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))    
    
    
elif choose == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

#It is important to show invalin in every code 
else:
    print("Invalid")

#Output message
print("Thanks For Joining With Us")
print("Hope You Have A Wounderful Day ")









    
