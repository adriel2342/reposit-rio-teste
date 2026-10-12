while True:
    print("===REGISTER===")
    Username = input ("set your username:").strip()
    Password = input("set your password: (ex: use numbers Uppercase and don't use personal informations):".strip())
    print("===REGISTER WAS SUCCESSFUL===")
    print("--- NOW CONFIRM YOUR INFORMATION---")
    Confirmation = input(f"is the {Username} right? (yes/no)").strip()
    if Confirmation == "yes" or Confirmation == "y":
        print("=== that`s right! now the password ===")
        PasswordConfirmation = input("confirm your password: ").strip()
        if PasswordConfirmation == Password:
            print("=== password confirmed! ===")
            print("=== REGISTER WAS SUCCESSFUL ===")
        elif PasswordConfirmation != Password:
            print("try again (last try, for security reasons)")
            PasswordConfirmation = input("confirm your password: ").strip()
            if PasswordConfirmation == Password:
                print("=== password confirmed! ===")
                print("=== REGISTER WAS SUCCESSFUL ===")
                print("==========================================")
                print("===               LOGIN                ===")
                UsernameLogin = input("insert your username: ").strip()
                if UsernameLogin == Username:
                    PasswordLogin = input("insert your password: ").strip()
                    if PasswordLogin == Password:
                        print("=== LOGIN WAS SUCCESSFUL, (you can now acess your account) ===")
                        break
                    else:
                        print("=== password mismatch! ===")  
                        print("=== please try again ===")
                else:
                    print("=== username mismatch! ===")  
                    print("=== please try again ===")
        else:
            print("=== password mismatch! ===")  
            print("=== please try again ===")
    elif Confirmation == "no" or Confirmation == "n":
        print("=== please try again ===")
        Username = input("insert again your username: ").strip()
        Confirmation = input(f"is the {Username} right? (yes/no)").strip()
        if Confirmation == "yes" or Confirmation == "y":
            print("=== that`s right! now the password ===")
            PasswordConfirmation = input("confirm your password: ").strip()
            if PasswordConfirmation == Password:
                print("=== password confirmed! ===")
                print("=== REGISTER WAS SUCCESSFUL ===")
                break
            elif PasswordConfirmation != Password:
                print("try again (last try, for security reasons)")
                PasswordConfirmation = input("confirm your password: ").strip()
                if PasswordConfirmation == Password:
                    print("=== password confirmed! ===")
                    print("=== REGISTER WAS SUCCESSFUL ===")
                    break
                else:
                    print("=== password mismatch! ===")  
                    print("=== please try again ===")

        elif Confirmation == "no" or Confirmation == "n":
            print("=== please try again ===")
            continue
        else:
            print("=== invalid input! please answer with Yes or No ===")
    else:
        print("=== invalid input! please answer with Yes or No ===")
