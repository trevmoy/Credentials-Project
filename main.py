"""
Main function
"""
from Credentials import credentials

def main(): 
    """
    Main function

    Declaring variables and objects
    """
    userChoice: str
    passChoice: str
    user = credentials()
    userChoice = input("Would you like a randomly generated username? ")
    if(userChoice != "yes" and userChoice != "Yes"):
        un = input("Please enter your custom username here: ")
    else:
        un = user.genUsername()
        print(un)
        

    passChoice = input("Would you like a randomly generated password? ")
    if(passChoice != "yes" and passChoice != "Yes"):
        pw = input("Please enter your custom username here: ")
    else:
        pw = user.genPassword()
        print(pw)

main()