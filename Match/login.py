username=input("Enter username: ")
password=input("Enter password: ")

match (username, password):
    case ("admin","admin123"):
        print("Login successful")
    case _:
        print("Invalid credentials")
    