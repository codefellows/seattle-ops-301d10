# The Python module “os” must be utilized.
# import the os module
import os
# import the time module
import time
# impor the sys module
import sys

# Requirements:

# At least three variables must be declared and referenced in Python.
def get_user_name():
    user_name = input("Please enter your name: ")
    return user_name


# The Python function print() must be used at least three times.
# Include execution of the following bash commands inside your Python script:

# function for menu passing in the user as a parameter
def menu(user):
    # Sart the while loop
    while True:
        # set variable for user name
        message = "Hello " + user + ". Lets try some commands"
        # print the message and menu
        print(message)
        print('1. whoami')
        print('2. ip a ')
        print('3. lshw -short')
        print('4. Exit')
        # Get user answer and assign in to the anser variable
        answer = input("What do you want to do? ")
        # conditional check of answers
        if answer == '1':
            # runs the bash command
            os.system('whoami')
            # waits for user to press enter to continue
            input('Press Enter to continue')
            # clears the screen
            os.system('clear')
        elif answer == '2':
            # adjusted for mac
            os.system('ifconfig')
            input('Press Enter to continue')
            os.system('clear')
        elif answer == '3':
            # adjusted for mac
            os.system('system_profiler SPHardwareDataType SPMemoryDataType SPPCIDataType SPAudioDataType')
            input('Press Enter to continue')
            os.system('clear')
        elif answer == '4':
            sys.exit('\nHave a Great Day')
        # catch all in case they don't enter 1-4   
        else:
            print("Not a valid choice, try again")
            time.sleep(2)
            os.system('clear')

# main gate function
if __name__ == "__main__":
    user  = get_user_name()
    menu(user)
