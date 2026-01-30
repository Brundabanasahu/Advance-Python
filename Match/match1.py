choice=input("Enter your choice:\n1.tea\n2.coffee\n3.soup\n")
match choice:
    case "tea":
        print("You have selected Tea")
    case "coffee":
        print("You have selected Coffee")
    case "soup":
        print("You have selected Soup")
    case _:
        print("Invalid choice")
