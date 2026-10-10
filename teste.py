while True:
    print("===CASDASTRO===")
    Username = input ("set your username:")
    Password = input("set your password: (ex: use numbers Uppercase and don't use personal informations)")
    print("===REGISTER WAS SUCCESSFUL===")
    print("--- NOW CONFIRM YOUR INFORMATION---")
    print("Username")
    confirmation = input(f"is the {Username} right? (Yes/No)").strip().upper()
        if confirmation == "YES" or "Y":
            print("=== that`s right! now the password ===")
            print("Password")
    elif confirmation == "NO" or "N": 
        print("=== please try again ===")
        confirmation = input(f"is the {Password} right? (Yes/No)").strip().upper()
        if confirmation == "YES" or "Y":
            print("=== that`s right! now you can login ===")
            break
        else:
            print("=== please try again ===")
       