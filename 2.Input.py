#The input() function allows user input.
#Prompts the user to enter an input
#default datatype for input() is String

name=input("What is your name?")
print('Hello, ' + name)

# if we wanna take a different datatype input, we need to do type casting
#Integer
number = int(input("Enter a number:"))
print("The number entered is: ",number)

#Floating point Number
floatNum = float(input("Enter a decimal number: ")) 
print(floatNum, " ", type(floatNum)) 

#checking the datatype
num = input ("Enter number :") 
print(num) 
name1 = input("Enter name : ") 
print(name1) 
  
# Printing type of input value 
print ("type of number", type(num)) 
print ("type of name", type(name1)) 

#raw_input(): This function works in older version (like Python 2.x). 
# This function takes exactly what is typed from the keyboard, converts it to string, and then returns it to the variable in which we want to store it.
#g = raw_input("Enter your name : ") 
#print g 




