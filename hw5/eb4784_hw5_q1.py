from ArrayStack import *
 
def evaluate(expr, variables):
    s = ArrayStack()
    for token in expr.split():
        if token in '+-*/':
            right = s.pop()
            left = s.pop()
            if token == '+':
                s.push(left + right)
            elif token == '-':
                s.push(left - right)
            elif token == '*':
                s.push(left * right)
            else:
                s.push(left / right)
        elif token in variables:
            s.push(variables[token])
        elif '.' in token:
            s.push(float(token))
        else:
            s.push(int(token))
    return s.pop()
 
def main():
    variables = {}
    line = input('--> ')
    while line != 'done()':
        tokens = line.split()
        if len(tokens) >= 2 and tokens[1] == '=':
            name = tokens[0]
            variables[name] = evaluate(' '.join(tokens[2:]), variables)
            print(name)
        else:
            print(evaluate(line, variables))
        line = input('--> ')
 
if __name__ == '__main__':
    main()