# Uses input to collect data from the user
first_name = input("What is your first name?    ")
last_name = input("What is your last name?  ")
age = int(input("What is your age?  "))
salary = int(input("What is your salary?    £"))
date_of_birth = input("What is your date? (dd/mm/yy)    ")
post_code = input("What is your post code?  ")

# Prints all the information collected from the user
print(first_name, last_name, "is", age, "has a salary of £", salary, "a date of birth of", date_of_birth, "and a post code of", post_code)