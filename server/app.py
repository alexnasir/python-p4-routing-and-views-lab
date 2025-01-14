from flask import Flask

app = Flask(__name__)



# Index view: Base URL
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string view: Prints a string to the console and browser
@app.route('/print/<string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(0, num + 1))
    return numbers

# Math view: Perform a math operation based on the URL parameters
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' and num2 != 0:
        result = num1 / num2
    elif operation == '%' and num2 != 0:
        result = num1 % num2
    else:
        return 'Invalid operation or division by zero'
    
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
