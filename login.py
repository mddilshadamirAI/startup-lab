# To ask for credential
userid = input("Enter your user id-")
correct_passwords = "password123,12345,926272,993142"
max_attempts = 5

for attempt in range(max_attempts):
    password = input("Enter your password-")
    if password in correct_passwords.split(','):
        print("        CONGRATULATIONS         ")
        print("Access granted")
        break
    else:
        remaining_attempts = max_attempts - (attempt + 1)
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempts remaining.")
        else:
            print("Maximum attempts reached. Access denied.")
else:
    print("login failed") 



 