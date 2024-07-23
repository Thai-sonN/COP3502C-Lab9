#Thai-Son's main file

def encode(password):
    encoded_password = ""
    for num in password:
        encoded_digit = int(num) + 3
        encoded_password += str(encoded_digit)
    return encoded_password



if __name__ == "__main__":
    menu = ("\nMenu\n"
            "-------------\n"
            "1. Encode\n"
            "2. Decode\n"
            "3. Quit\n")
    og_password = ""
    ec_password = ""

    while True:
        print(menu)
        selection = int(input("Please enter an option: "))
        if selection == 1:
            og_password = input("Please enter the password to encode: ")
            ec_password = encode(og_password)
            print("Your password has been encoded and stored!")
        elif selection == 2 and og_password:
            print(f"The encoded password is {ec_password}, and the original password is {decode(ec_password)}.")
        elif selection == 2 and not og_password:
            print("No original password stored")
        elif selection == 3:
            exit(0)
        else:
            print("Option not recognized.")