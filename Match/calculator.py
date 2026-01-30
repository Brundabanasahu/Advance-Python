cal=input("Enter the calculation (+, -, *, /): ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
match cal:
    case "+":
        print("the sum is", num1 + num2)
    case "-":
        print("the difference is", num1 - num2)
    case "*":
        print("the product is", num1 * num2)
    case "/":
        print("the quotient is", num1 / num2)
    case "%":
        print("the remainder is", num1 % num2)
    case _:
        print("Invalid operation")                   