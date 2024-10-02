#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    # Print the given string to the console
    print(f'{string}')
    # Display string in browser
    return string

@app.route('/count/<int:number>')
def count(number):
    # Create a list with numbers from 0 to the given number, separated by newlines
    numbers = '\n'.join(str(i) for i in range(number)) + '\n'
    return numbers

@app.route('/math/<num1>/<operator>/<num2>')
def math(num1, operator, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == 'div':
            if num2 == 0:
                return 'Error: Division by zero'
            result = num1 / num2
            return str(float(result))
        elif operator == '%':
            result = num1 % num2
            return str(int(result))  # Return as int for whole numbers
        else:
            return 'Error: Invalid operator'
        
        return str(int(result)) if result.is_integer() else str(result)
    
    except ValueError:
        return 'Error: Invalid input'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
