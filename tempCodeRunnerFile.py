while True:
    print("===CADASTRO===")
    Username = input("set your username: ").strip()
    Password = input("set your password: (ex: use numbers Uppercase and don't use personal informations): ").strip()
    print("===REGISTER WAS SUCCESSFUL===")
    print("--- NOW CONFIRM YOUR INFORMATION---")
    print("Username")
    Confirmation = input(f"is the {Username} right? (yes/no)").strip()
    
    # 1. Se o primeiro username estiver correto ("yes" ou "y")
    if Confirmation == "yes" or Confirmation == "y":
        print("=== that's right! now the password ===")
        print("Password")
        PasswordConfirmation = input("confirm your password: ").strip()
        
        if PasswordConfirmation == Password:
            print("=== password confirmed! ===")
            print("=== REGISTER WAS SUCCESSFUL ===")
            break
        elif PasswordConfirmation != Password:
            print("try again (last try, for security reasons)")
            passwordConfirmation = input("confirm your password: ").strip()
            if passwordConfirmation == Password:
                print("=== password confirmed! ===")
                print("=== REGISTER WAS SUCCESSFUL ===")
                break
            else:
                print("=== password mismatch! ===")
                print("=== please try again ===")
        else:
            print("=== password mismatch! ===")
            print("=== please try again ===")

    # 2. Se o primeiro username estiver errado ("no" ou "n")
    elif Confirmation == "no" or Confirmation == "n":
        print("=== please try again ===")
        Username = input("insert again your username: ").strip()
        print("Username")
        Confirmation = input(f"is the {Username} right? (yes/no)").strip()
        
        # Confirmação do NOVO username digitado
        if Confirmation == "yes" or Confirmation == "y":
            print("=== that's right! now the password ===")
            print("Password")
            PasswordConfirmation = input("confirm your password: ").strip()
            
            if PasswordConfirmation == Password:
                print("=== password confirmed! ===")
                print("=== REGISTER WAS SUCCESSFUL ===")
                break
            else:
                print("try again (last try, for security reasons)")
                passwordConfirmation = input("confirm your password: ").strip()
                if passwordConfirmation == Password:
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