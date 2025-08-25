import os

#check character to see if it can become a float
def can_convert(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#convert string to list of chars and floats
def converter():
    user = input("Enter Equation: ")
    equation = user.split(" ")

    for i in range(len(equation)):
        if can_convert(equation[i]):
            equation[i] = float(equation[i])

    return(equation)

#handle paranthesis
def paranthesis(e):
    i_start = 0
    if not '(' in e:
        return e
    #assign a list for storing paranthesis
    para = []
    #for loop checks if a '(' is in the list and stores the equation within the list for paranthesis
    for i in range(len(e)):
        if e[i] == '(':
            i += 1
            while i < len(e) and e[i] != ')':
                para.append(e[i])
                i += 1

    #solves equation within parathesis
    para = exponent(para)
    para = multiply_divide(para)
    para = add_subtract(para)

    #insert solved parathesis within the main equation list
    for i in range(len(e)):
        if e[i] == '(':
            j = e.index(')', i)
            e[i:j+1] = [para[0]]
            break
    return e

#handle exponents
def exponent(e):
    for i in range(len(e)):
        if not '(' in e or ')' in e:
            if '^' in str(e[i]):
                e[i] = pow(float(e[i][0]), float(e[i][2]))
    return e

#handle multiplication and division
def multiply_divide(e):
    i = 0
    while i < len(e):
        if not '^' in e or '(' in e or ')' in e:
            if '*' in str(e[i]):
                e[i] = e[i-1] * e[i+1]
                del e[i-1]
                del e[i]
            elif '/' in str(e[i]):
                e[i] = e[i-1] / e[i+1]
                del e[i-1]
                del e[i]
            else:
                i += 1
                continue
    return e

#handle addition and subtraction
def add_subtract(e):
    i = 0
    while i < len(e):
        if not '^' in e or '(' in e or ')' or '*' in e or '/' in e:
            if '+' in str(e[i]):
                e[i] = e[i-1] + e[i+1]
                del e[i-1]
                del e[i]
            elif '-' in str(e[i]):
                e[i] = e[i-1] - e[i+1]
                del e[i-1]
                del e[i]
            else:
                i += 1
                continue
    return e

#main function
def main():
    equation = converter()
    equation = paranthesis(equation)
    equation = exponent(equation)
    equation = multiply_divide(equation)
    equation = add_subtract(equation)
    return(equation)

#main loop
while True:
    sol = main()
    if sol == ['quit']:
        break
    elif sol == ['clear']:
        os.system('clear')
    sol = str(sol).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
    print(sol)
