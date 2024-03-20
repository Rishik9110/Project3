from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/luv',methods=['GET'])
def luv():
    return render_template('response.html',context="I Am yours...")

@app.route('/luv2',methods=['GET'])
def luv2():
    return render_template('response.html',context="You Are Mine...")

@app.route('/',methods=['GET'])
def home():
    return "WElcome"



@app.route('/add',methods=['GET'])
def Addition():
    return render_template("form.html",operation="Addition-form",path="/addition_form")

@app.route('/addition_form',methods=['POST'])
def addition_form():
    num1 = request.form['a']
    num2 = request.form['b']
    num1 = int(num1)
    num2 = int(num2)
    result = f'The addition of {num1} and {num2} is {num1+num2}'
    return render_template("response.html",context=result)





@app.route('/sub',methods=['GET'])
def subtraction():
    return render_template("form.html",operation="Subtraction-form",path="/subtraction_form")

@app.route('/subtraction_form',methods=['POST'])
def subtraction_form():
    num1 = request.form['a']
    num2 = request.form['b']
    num1 = int(num1)
    num2 = int(num2)
    result = f'The subtraction of {num1} and {num2} is {num1-num2}'
    return render_template("response.html",context=result)





@app.route('/mul',methods=['GET'])
def multiplication():
    return render_template("form.html",operation="Multiplication-form",path="/multiplication_form")

@app.route('/multiplication_form',methods=['POST'])
def multiplication_form():
    num1 = request.form['a']
    num2 = request.form['b']
    num1 = int(num1)
    num2 = int(num2)
    result = f'The multiplication of {num1} and {num2} is {num1*num2}'
    return render_template("response.html",context=result)





@app.route('/div',methods=['GET'])
def division():
    return render_template("form.html",operation="Division-form",path="/division_form")

@app.route('/division_form',methods=['POST'])
def division_form():
    num1 = request.form['a']
    num2 = request.form['b']
    num1 = int(num1)
    num2 = int(num2)
    result = f'The division of {num1} and {num2} is {num1/num2}'
    return render_template("response.html",context=result)





app.run()