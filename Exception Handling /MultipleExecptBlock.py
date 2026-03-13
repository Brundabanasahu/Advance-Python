#Multiple Exceptions with single TRY

'''

try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = a/b
    print(a)
    print(b)

except ZeroDivisionError as z:
    print(z)

except ValueError as v:
    print(v)

'''


try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = a/b
    print(a)
    print(b)

except (ZeroDivisionError, ValueError):
    print("There may be Division by Zero or Data type of both variable should be same")