#!c:\Python38\lib python3.8

from user import User
from credential import Credential

user_list = []
cred_list = []

def create_user(name, password):
    '''
    Function to create users
    '''
    new_user = User(name, password)
    return new_user

def create_credential(name):
    '''
    Function to create user's credential
    '''
    new_credential = Credential(name)
    return new_credential



def list_credentials():
    for cred in cred_list:
        print(cred.username + " " + cred.password)



def main():
    '''
    Entry point to our application
    '''
    print("Hello: Welcome to our password Vault System")
    print("-------------------------------------")
    print("First create an account. Please enter your user name")

    name = input()

    print("\n")
    print("Enter your password")
    password = input()

    user_list.append(create_user(name, password))
    
    cred_list.append(create_credential(name))

    print("\n")
    print("\n")
    print("Would you like to enter more website credentials?")
    print("1: Yes 2: No")
    sel_option = input()

    if sel_option == 1:
        print("Enter website name:")

        website = input()

        print("Enter password:")

        pwd = input()
    
    elif sel_option == 2:
        print("Display credentials:Y/N")

        sel_option2 = input()

        if sel_option2 == "Y":
            list_credentials()

        elif sel_option2 == "N":
            exit()
        



if __name__ == '__main__':

    main()


