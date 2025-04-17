def check_password():
    correct_password = "SH404"
    try:
        user_input = input("Enter Admin Password: ")
        return user_input == correct_password
    except KeyboardInterrupt:
        print("\nAborted.")
        return False
