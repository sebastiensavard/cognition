def check_for_69():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        if number == 69:
            print("You entered the number 69!")
        else:
            print("You did not enter the number 69.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Test the function
check_for_69()
