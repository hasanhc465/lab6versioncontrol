#hasan cakar

#function for encoding user input password
def encode(password):
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


#function for decoding encoded password from user input
def decode(password):
    ### COP3502C | LEO JO | OCT.25.2023 ###
    de_pass = ""
    for i in password:
        i = (int(i) + 10) - 3
        if i > 10:
            i -= 10
        i = str(i)
        de_pass += i
    return de_pass

#main function that prints menu options and ask for user menu option
def main():
    password = ''
    decoded = ''
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
        print()
        user_op = int(input("Please enter an option: "))
        #gets more info in order to call encoder function and stores new password
        if user_op == 1: #menu option to encode password
            password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print()
        elif user_op == 2:#menu option to get the original password
            decoded = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded}.")
            print()
        elif user_op == 3: #menu option to quit menu
            break

#runs main function
if __name__ == "__main__":
    main()
