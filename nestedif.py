print("Enter your age: ")
age = int(input())
if age >= 18:
    if age >= 65:
        print("You are eligible to vote and also qualify for senior citizen benefits.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")        