
# Taking user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Creating full name
full_name = first_name.strip() + " " + last_name.strip()

# Displaying greeting message
print(f"\nHello, {full_name}! Welcome to Python programming!")
