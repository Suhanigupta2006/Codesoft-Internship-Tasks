def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def main():
    print("🔢 Simple Calculator in Python 🔢")

    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("👋 Exiting Calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                print(f"➕ Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"➖ Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"✖ Result: {num1} × {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"➗ Result: {num1} ÷ {num2} = {result}")
        else:
            print("❌ Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()