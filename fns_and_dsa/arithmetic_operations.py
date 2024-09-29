def perform_operation(num1 , num2, operation):
    match operation:
        case "addi":
            result = num1 + num2
            return result
        case "subtract":
            result = num1 - num2
            return result
        case "mutltiply":
            result = num1 * num2
            return result
        case "divide":
            result = "You can't divede with zero." if nuum2 == 0 else num1 / num2
            return result
