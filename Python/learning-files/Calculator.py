def calculator():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operator = input("Enter operator: ")
    match operator:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1/num2)
        case "%":
            print(num1%num2)

calculator()