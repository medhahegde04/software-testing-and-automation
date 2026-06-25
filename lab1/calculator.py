def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    expr = input("Enter expression (e.g. 3 + 4): ").strip().split()
    if len(expr) != 3:
        print("Usage: number operator number")
        return
    try:
        a = float(expr[0])
        op = expr[1]
        b = float(expr[2])
        if op not in ops:
            print("Operator must be one of + - * /")
            return
        result = ops[op](a, b)
        print(result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
