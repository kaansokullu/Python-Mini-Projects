import calculator_art

def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    if num_2 == 0.0:
        return ZeroDivisionError
    return num_1 / num_2

def exponentiation(num_1, num_2):
    if num_1 == 0.0:
        if num_2 == 0.0:
            return "Indeterminate"
        elif num_2 < 0:
            return "Undefined"
    return num_1 ** num_2

def modulo(num_1, num_2):
    if num_2 == 0.0:
        return ZeroDivisionError
    return num_1 % num_2

def num_ctrl(number):
    while True:
        try:
            number = float(number)
            return number
        except ValueError:
            print("Invalid entry! Please try again entering a number.")
            number = input("Enter a number: ")

math_dict = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division,
    "**" : exponentiation,
    "%" : modulo
}

while True:
    print(calculator_art.logo)
    first_number = num_ctrl(input("What is your first number: "))

    for key in math_dict.keys():
        print(key)

    while True:
            sign = input("Pick the arithmetic operation: ")
            if sign in math_dict:
                break
            else:
                print("Invalid entry! Please try again.")

    second_number = num_ctrl(input("What is your second number: "))
    result = math_dict[sign](first_number, second_number)
    print(f"{first_number} {sign} {second_number} = {result}")

    lst = ['y', 'n', 'q']

    while True:
        flag = input(f"Type 'y' to continue calculatin with {result:.3f}, type 'n' to start a new calculation, or type 'q' to quit calcultion: ").lower()
        if flag in lst:
            break
        else:
            print("Invaild entry! Try again.")

    while flag == 'y':
        first_number = result

        for key in math_dict.keys():
            print(key)

        while True:
            sign = input("Pick the arithmetic operation: ")
            if sign in math_dict:
                break
            else:
                print("Invalid entry! Please try again.")
        
        second_number = num_ctrl(input("What is your next number: "))
        result = math_dict[sign](first_number, second_number)
        print(f"{first_number} {sign} {second_number} = {result}")

        while True:
                flag = input(f"Type 'y' to continue calculatin with {result:.3f}, type 'n' to start a new calculation, or type 'q' to quit calcultion: ").lower()
                if flag in lst:
                    break
                else:
                    print("Invalid entry! Try again.")

    if flag == 'q':
        print("Calculation is over, goodbye. ☺")
        break
    else:
        print("\n"*50)