def can_convert(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def converter():
    user = input("Enter Equation: ")
    equation = user.split(" ")

    for i in range(len(equation)):
        if can_convert(equation[i]):
            equation[i] = float(equation[i])

    return(equation)

#handle exponents
def exponent(e):
    for i in range(len(e)):
        if not '(' in e or ')' in e:
            if '^' in str(e[i]):
                e[i] = pow(float(e[i][0]), float(e[i][2]))
    return e

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

def main():
    equation = converter()
    equation = exponent(equation)
    equation = multiply_divide(equation)
    equation = add_subtract(equation)
    return(equation)

while True:
    sol = main()
    if sol == ['quit']:
        break
    sol = str(sol).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
    print(sol)
