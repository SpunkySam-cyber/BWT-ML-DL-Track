def user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    fav_no = input("Enter your favorite number: ")
    return name, age, email, fav_no

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

def main():
    name, age, email, fav_no = user_info()
    
    while not validate_email(email):
        print("Invalid email. Enter valid email.")
        email = input("Enter your email: ")
    
    user_info_dict = {
        "name": name,
        "age": age,
        "email": email,
        "fav_no": fav_no
    }
    
    message = f"Hello {user_info_dict['name']}, you are {user_info_dict['age']} years old, your email is {user_info_dict['email']} and your favorite number is {user_info_dict['fav_no']}."
    print(message)

if __name__ == "__main__":
    main()
