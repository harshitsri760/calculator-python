# ============ Calculator ==============

# 🎯 Features
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulus
# 6. Power
# 7. Invalid operator handling

# # input -------
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /, %, **): ")

# # function ---------
# def calculator(a, b, operator):

#     if operator == "+":
#         return a + b

#     elif operator == "-":
#         return a - b

#     elif operator == "*":
#         return a * b

# # Division aur modulus se pehle zero check :
#     elif operator == "/":
#         if b==0:
#             return "division not allow with denominator zero"
#         return a / b

#     elif operator == "%":
#         if b==0:
#             return "modulus not allow with zero" 
#         return a % b

#     elif operator == "**":
#         return a ** b

#     else:
#         return "Invalid operator"

# # function call --------
# result = calculator(num1, num2, operator)

# print("Result:", result)


# ============ Calculator Version 2 ==============

def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    elif operator == "%":
        if b == 0:
            return "Cannot calculate modulus with zero"
        return a % b

    elif operator == "**":
        return a ** b

    else:
        return "Invalid operator"


# ============ Main Program ==============

while True:

    print("\n===== CALCULATOR =====")
    print("Type 'exit' to close calculator")

    num1 = input("Enter first number: ")

    if num1.lower() == "exit":
        print("Calculator closed")
        break

    num2 = input("Enter second number: ")

    if num2.lower() == "exit":
        print("Calculator closed")
        break

    operator = input("Enter operator (+, -, *, /, %, **): ")

    if operator.lower() == "exit":
        print("Calculator closed")
        break

    num1 = float(num1)
    num2 = float(num2)

    result = calculator(num1, num2, operator)

    print("Result:", result)