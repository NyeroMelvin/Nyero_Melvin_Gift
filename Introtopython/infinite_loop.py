while True:
    try:
        num1_str = input("Enter the first number: ")
        num2_str = input("Enter the second number: ")

        num1 = float(num1_str) 
        num2 = float(num2_str)

        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")

        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break  

    except ValueError:
        print("Invalid input. Please enter valid numbers only.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print("Program execution finished.")