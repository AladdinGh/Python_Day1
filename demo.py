def calculator():
    """A simple calculator that takes two numbers and an operand."""
    print("\n🧮 Basic Calculator\n")
    

    
    try:
        # Get first number
        num1 = float(input("Enter first number: "))
        
        # Get operand
        operand = input("Enter operand (+, -, *, /): ").strip()
        
        # Get second number
        num2 = float(input("Enter second number: "))
        
        # Perform calculation
        if operand == '+':
            result = num1 + num2
        elif operand == '-':
            result = num1 - num2
        elif operand == '*':
            result = num1 * num2
        elif operand == '/':
            if num2 == 0:
                print("❌ Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("❌ Invalid operand! Use +, -, *, or /")
            return
        
        # Display result
        print(f"\n✓ Result: {num1} {operand} {num2} = {result}\n")
    
    except ValueError:
        print("❌ Error: Please enter valid numbers!\n")

if __name__ == "__main__":
    calculator()
