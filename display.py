import time

def display_welcome():
    print("\n" * 10) 
    print("**********************************************")
    print("*                                            *")
    print("*         WELCOME TO THE QUIZ GAME!          *")                             
    print("*                                            *")
    print("**********************************************\n")
    print("Test your knowledge and win!!!\n")
    print("Instructions:")
    print("- Multiple-choice or open-ended questions")
    print("- Answer by typing the option number or text")
    print("- Type 'quit' anytime to exit\n")

    user_name = input("Enter your name: ")
    print(f"\nWelcome {user_name}, let's begin the game!")
    time.sleep(2)
    print("\n" * 10)
