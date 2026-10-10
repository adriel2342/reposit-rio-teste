while True:
    print("===CADASTRO===")
    Username = input ("set your username:").strip()
    Password = input("set your password: (ex: use numbers Uppercase and don't use personal informations):".strip())
    print("===REGISTER WAS SUCCESSFUL===")
    print("--- NOW CONFIRM YOUR INFORMATION---")
    print("Username")
    Confirmation = input(f"is the {Username} right? (yes/no)").strip()
    if Confirmation == "yes" or Confirmation == "y":
        print("=== that`s right! now the password ===")
        print("Password")
        PasswordConfirmation = input("confirm your password: ").strip()
        if PasswordConfirmation == Password:
            print("=== password confirmed! ===")
            print("=== REGISTER WAS SUCCESSFUL ===")
            break
        else:
            print("=== password mismatch! ===")   
    elif Confirmation == "no" or Confirmation == "n":
        print("=== please try again ===")
    else :
        print("=== invalid input! please answer with Yes or No ===")
        
    