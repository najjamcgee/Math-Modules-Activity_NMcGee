#Name: Najja McGee
#Date: June 18th, 2023
#Course: CIS 111
#Section: Math Module
#Program Name: Math Modules Activity     

#Algorithm
#Step 1: Prompt the user to enter a float as a ciel function
#Step 2: Display the ciel function
#Step 3: Prompt the user to enter a negative number for fabs function
#Step 4: Display the fabs function
#Step 5: Prompt the user to enter a number for the square root function
#Step 6: Display the square root function
#Step 7: Prompt the user to enter two numbers for the power function
#Step 8: Display the power function
#Step 9: Prompt the user to enter a number for the exponent function
#Step 10: Display the exponent function
#Step 11: Prompt the user to enter a number for the factorial function
#Step 12: Display the factorial function
#Step 13: Prompt the user to enter a number for the floor function
#Step 14: Display the floor function
#Step 15: Prompt the user to enter a number for the fmod function
#Step 16: Display the fmod function
#Step 17: Prompt the user to enter a number for the round function
#Step 18: Display the round function
import math
#find the function of ceil
print("find the function of ceil")
ceil_number = float(input("Enter a float: "))
print(math.ceil(ceil_number))
print()

#find the function of fabs
print("find the function of fabs")
fabs_number = int(input("Enter a negative number: "))
print(math.fabs(fabs_number))
print()

#find the function of square root
print("find the function of square root")
sqrt_number = int(input("Enter a number: "))
print(math.sqrt(sqrt_number))
print()

#find the power
print("find the power")
pow_num1 = int(input("Enter a number: "))
print()
print("Enter a second number")
pow_num2 = int(input("Enter a number: "))
print(math.pow(pow_num1, pow_num2))
print()

#find the exponent
print("find the exponent")
exp_number = int(input("Enter a number: "))
print(math.exp(exp_number))
print()

#find the factorial
print("find the factorial")
factorial_number = int(input("Enter a number: "))
print(math.factorial(factorial_number))
print()

#find the floor
print("find the floor")
floor_number = float(input("Enter a float: "))
print(math.floor(floor_number))
print()

#find the fmod
print("find the fmod")
fmod1_number = int(input("Enter a x value: "))
fmod2_number = int(input("Enter a y value: "))
print(math.fmod(fmod1_number, fmod2_number))
print()

#find the round 
print("find the round")
round_num1 = float(input("Enter a float number: "))
round_num2 = int(input("Enter a number: "))
print(round(round_num1, round_num2))