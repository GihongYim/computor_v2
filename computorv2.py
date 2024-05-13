

def get_number(expr: str):
    
    return 1

def computorv2():
    variable = {}
    while True:
        expression = input('> ')
        expression = expression.strip()
        if expression == 'exit':
            break
        expr = expression.split('=')
        variable[expr[0].strip()] = get_number(expr[1].strip())
        print(variable)
if __name__ == "__main__":
    computorv2()