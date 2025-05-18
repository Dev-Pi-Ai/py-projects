def calculator(equation):
    equation = equation.replace(" ", "")
    if '+' in equation:
        array = equation.split("+")
        result = int(array[0]) + int(array[1])
        return result
    if "-" in equation:
        array = equation.split("-")
        result = int(array[0]) - int(array[1])
        return result
    if "*" in equation:
        array = equation.split("*")
        result = int(array[0]) * int(array[1])
        return result
    if "/" in equation:
        array = equation.split("/")
        result = int(array[0]) / int(array[1])
        return result
    if "%" in equation:
        array = equation.split("%")
        result = int(array[0]) / int(array[1]) * 100
        return str(result) + "%"
        
while True:
    equation = str(input("> "))
    if "exit" in equation:
        break
    print(calculator(equation))