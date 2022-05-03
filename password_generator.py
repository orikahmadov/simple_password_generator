"""Script that asks user to enter a length of password and then it generates a random password of that length by using uppercase and special
characters and numbers."""


def main():
    import random
    import string

    terminated =  False
    while not terminated: # Loop until user terminates the program
        length_pasword = int(input("Enter the length of password: "))
        if length_pasword < 8 or type(length_pasword) != int: # Check if the length of password is less than 8 or not an integer   
            print("Password length should be at least 8 characters long.")
        else:
            password = ''.join(random.choice(string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase) for _ in range(length_pasword))
            print("Your password is: ", password)
            #asks user if he wants to generate another password
            another_password = input("Do you want to generate another password? (y/n): ")
            if another_password == "y" or another_password == "Y":
                continue
            elif another_password == "n" or another_password == "N":
                print("Thank you for using the password generator.")
                terminated = True
                break
            else:
                print("Invalid input. Please enter y or n.")
                continue


            
            


if __name__ == '__main__':
    main()

    
