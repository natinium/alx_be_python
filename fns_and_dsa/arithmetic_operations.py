def perform_operation(num1 , num2, operation):
    match operation:
        case "add":
            result = num1 + num2
            return result
        case "subtract":
            result = num1 - num2
            return result
        case "multiply":
            result = num1 * num2
            return result
        case "divide":
            result = "You can't divede with zero." if num2 == 0 else num1 / num2
            return result
        case _:
            return "Error: Invalid operation"
