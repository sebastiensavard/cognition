print("Hello World")
print("69")
def check_number():
    """
    Prompt the user to input a number and check if it matches a specific value.

    Returns:
    bool: True if the number matches the specific value, False otherwise.
    """
    # Ask the user to input a number
    num = input("Please enter a number: ")

    # Check if the input number matches the specific value
    specific_value = 69  # Change this to whatever specific value you want to check
    if int(num) == specific_value:
        return True
    else:
        return False

# Call the function and check the result
if check_number():
    print("The number matches the specific value.")
else:
    print("The number is not 69.")
