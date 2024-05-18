def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    
    while True:
        print("Simple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice : ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"The result is : {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is : {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is : {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"The result is : {num1} / {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter numerical values.")

        else:
            print("Invalid choice! Please select a valid operation.")

        next = input("Do you want to perform another calculation? (y/n): ")
        if next.lower() != 'y':
            break

if __name__ == "__main__":
    main()
