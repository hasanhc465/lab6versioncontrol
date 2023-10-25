#hasan cakar

#function for encoding user input password
def encoder(password):
    new_pass = []
    if len(password) == 8 and password.isdigit():
        for digit in password:
            digit = int(digit)
            digit += 3
            digit = str(digit)
            new_pass.append(digit)
        return ''.join(new_pass)
    else:
        raise ValueError

#main function that prints menu options and ask for user menu option
def main():
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
        print()
        user_op = int(input("Please enter an option: "))
        #gets more info in order to call encoder function and stores new password
        #include try and except for valueerror
        if user_op == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoder(password)
            print()
        #elif user_op == 2: where decoding user op will go

        elif user_op == 3:
            break

#runs main function
if __name__ == "__main__":
    main()
