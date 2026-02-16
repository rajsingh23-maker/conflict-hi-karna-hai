def subtract(a, b):
    return a - b


def main():
    print("Subtraction Program")
    
    # Taking input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = subtract(num1, num2)
    
    print("Result:", result)


if __name__ == "__main__":
    main()
