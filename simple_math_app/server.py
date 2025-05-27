from flask import Flask, render_template, request
from Maths.mathematics import addition, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except TypeError:
        return "Both Number 1 and Number 2 must be entered.", 400
    result = addition(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except Exception:
        return "Both Number 1 and Number 2 must be entered.", 400
    result = subtraction(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/mul")
def mul_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except TypeError:
        return "Both Number 1 and Number 2 must be entered.", 400
    result = multiplication(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/")
def render_index_page():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
