"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your codeq




while True:
    # Read user input
    # user can quit, quit the program ('q')
    data = input("Give us Equation : ")
    if data == 'q':
        break
    # commands will be seperated by space, so we can split on spaces
    # Whole numbers only
    list_data=data.split(" ")
    list_data[1] = float(list_data[1])

    if len(list_data)>2:
        list_data[2] = float(list_data[2])
    print(list_data)
    if list_data[0] == '+':
        print(add(list_data[1], list_data[2]))
    elif list_data[0]== '-':
        print(subtract(list_data[1],list_data[2]))
    elif list_data[0]== '*':
        print(multiply(list_data[1],list_data[2]))
    elif list_data[0] == '/':
        print(divide(list_data[1], list_data[2]))
    elif list_data[0] == 'square':
        print(square(list_data[1]))
    elif list_data[0] == 'cube':
        print(cube(list_data[1]))
    elif list_data[0] == 'pow':
        print(power(list_data[1], list_data[2]))
    elif list_data[0]== 'mod':
        print(mod(list_data[1],list_data[2]))
    else:
        print("Invalid entry! Please try again!")