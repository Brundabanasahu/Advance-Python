try:
    a = int(input("Enter the number: "))
    b = int (input("Enter the number: "))
    print(a+b)

except ValueError as c:
    print("Please Take the Numbers only eg: 1234")