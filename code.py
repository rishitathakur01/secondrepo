import math

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract y from x"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide x by y"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    """Calculate x to the power of y"""
    return x ** y

def square_root(x):
    """Calculate square root of x"""
    if x < 0:
        return "Error! Cannot calculate square root of negative number."
    return math.sqrt(x)

def modulo(x, y):
    """Calculate x modulo y"""
    if y == 0:
        return "Error! Modulo by zero."
    return x % y

def factorial(x):
    """Calculate factorial of x"""
    if x < 0:
        return "Error! Factorial not defined for negative numbers."
    if x != int(x):
        return "Error! Factorial only works with whole numbers."
    return math.factorial(int(x))

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("           ADVANCED CALCULATOR")
    print("="*50)
    print("Basic Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("\nAdvanced Operations:")
    print("  5. Power (x^y)")
    print("  6. Square Root (√x)")
    print("  7. Modulo (x % y)")
    print("  8. Factorial (x!)")
    print("\nOther:")
    print("  9. View History")
    print("  0. Exit")
    print("="*50)

def display_history(history):
    """Display calculation history"""
    if not history:
        print("\nNo calculations yet!")
        return
    
    print("\n" + "="*50)
    print("           CALCULATION HISTORY")
    print("="*50)
    for i, calc in enumerate(history, 1):
        print(f"{i}. {calc}")
    print("="*50)

def calculator():
    """Main calculator function"""
    history = []
    
    print("\nWelcome to the Advanced Calculator!")
    print("Made by: Your Name | B.Tech CSE AI | 2nd Year")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-9): ").strip()
        
        # Exit
        if choice == '0':
            print("\n" + "="*50)
            print("Thank you for using the calculator!")
            print("="*50)
            break
        
        # View History
        if choice == '9':
            display_history(history)
            continue
        
        # Operations requiring one number
        if choice == '6':
            try:
                num = float(input("\nEnter the number: "))
                result = square_root(num)
                calculation = f"√{num} = {result}"
                print(f"\nResult: {calculation}")
                if isinstance(result, (int, float)):
                    history.append(calculation)
            except ValueError:
                print("\nInvalid input! Please enter a valid number.")
            continue
        
        if choice == '8':
            try:
                num = float(input("\nEnter the number: "))
                result = factorial(num)
                calculation = f"{int(num)}! = {result}"
                print(f"\nResult: {calculation}")
                if isinstance(result, (int, float)):
                    history.append(calculation)
            except ValueError:
                print("\nInvalid input! Please enter a valid number.")
            continue
        
        # Operations requiring two numbers
        if choice in ['1', '2', '3', '4', '5', '7']:
            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    calculation = f"{num1} + {num2} = {result}"
                elif choice == '2':
                    result = subtract(num1, num2)
                    calculation = f"{num1} - {num2} = {result}"
                elif choice == '3':
                    result = multiply(num1, num2)
                    calculation = f"{num1} × {num2} = {result}"
                elif choice == '4':
                    result = divide(num1, num2)
                    calculation = f"{num1} ÷ {num2} = {result}"
                elif choice == '5':
                    result = power(num1, num2)
                    calculation = f"{num1}^{num2} = {result}"
                elif choice == '7':
                    result = modulo(num1, num2)
                    calculation = f"{num1} % {num2} = {result}"
                
                print(f"\nResult: {calculation}")
                if isinstance(result, (int, float)):
                    history.append(calculation)
                    
            except ValueError:
                print("\nInvalid input! Please enter valid numbers.")
        else:
            print("\nInvalid choice! Please select 0-9.")
        
        input("\nPress Enter to continue...")

# Run the calculator
if __name__ == "__main__":
    calculator()