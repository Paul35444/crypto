from sys import argv, exit
print("I know that these are the words the user typed on the command line: ", argv)

from helpers import rotate_character
message = input("Enter your message: ")
rot = int(input("How much do you want to rotate by? "))

def user_input_is_valid(cl_args):
    if (str(cl_args).isdigit()):
        return True
    # elif (len(cl_args) < 2):
    #     return False
    else:
        return False
    exit()

def main():

    input_valid = user_input_is_valid(args[1])

    if input_valid == True:
        msg = input("Type a message: \n")
        return(rotate_character(msg, int(args[1])))
    else:
        return("Usage: python3 caesar.py n")

print(rotate_character(message, rot))
