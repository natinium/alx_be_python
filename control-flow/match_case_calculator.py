num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = print("Cannot divide by zero.") if num2 == 0 else print("The result is " + str(quotient) + ".") 

match operation:
    case '+': print("The result is " + str(sum) + ".")
    case '-': print("The result is " + str(difference) + ".")
    case '*': print("The result is " + str(product) + ".")
    case '/': quotient
    case _ : print("NO such opperation")

