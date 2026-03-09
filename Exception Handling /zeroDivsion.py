try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = a/b
    print(a)
    print(b)

except ZeroDivisionError as z:
    print(z)