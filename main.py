
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    x = float(request.form['x'])
    y = float(request.form['y'])
    operator = request.form['operator']

    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        if y == 0:
            result = 'Error: Division by zero'
        else:
            result = x / y
    else:
        result = 'Invalid operator'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
