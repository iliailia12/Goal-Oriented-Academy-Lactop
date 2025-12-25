# 2) გადახედეთ შემდეგ კოდს და ახსენით თითოეული მოქმედება კომენტარებით:

# number = 5
# attempt = 3
# user_input = ""

# while user_input != number and attempt > 0:
#     user_input = int(input("Guess the number between 1-10: "))
#     attempt -= 1
    
#     if user_input == number:
#         print("You win!")
#     elif attempt == 0:
#         print("You lose!")
#     else:
#         print("Wrong number!")
#         print("You still have " + str(attempt) + " tries")



number = 5       
attempt = 3         
user_input = ""

while user_input != number and attempt > 0:

    user_input = int(input("Guess the number between 1-10: "))

    attempt -= 1
    
    if user_input == number:
        print("You win!")           

    elif attempt == 0:
        print("You lose!")         

    else:
        print("Wrong number!")     
        print("You still have " + str(attempt) + " tries")   
