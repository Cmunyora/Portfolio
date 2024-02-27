# Ask for the user's name and store it in a variable
name = input("What is your name? ").title()

# Ask for the user's age and store it as an integer
age = int(input("How old are you? "))

# Ask for the user's location
location = input("Where do you live? ").title()

# Print a personalized message using the collected information
print(f"Hello {name}, you are {age} years old and live in {location}.")
