##Section 1: Import the Class Libraray for generating a random number by the computer.
import random


##Section 2: 
#..Ceate an object for the computer to generate a random number. The randint issubclass will generate a number of 1 through 100. 
random_number =random.randint(1, 100)

#Create variable object for the end user. Do not set variable to a number between 1 and 100 so section 3 while loop can properly run.
guess = -1

##Section 3:
#While Loop Control Flow Header and Logic Test comparing the variable values.
while guess != random_number:
    
    #Reask the quesstion in the terminal from the end user and reassign the guess object bariable.
    #Reassign the guess object to the input from the end user.
    guess = int(input("Please Enter a Number Between 1 and 100:"))
    
    #Conditional logic to determine if the guess is too high or too low
    #If Scenario logic
    #Nested logic of the application:
    if guess < random_number:
        print("Number too low")
    elif guess > random_number:
        print("Number too high")
    else:
        print("Hooray, you have passed the right number!")
    
    
    
    
    
    
    
    
