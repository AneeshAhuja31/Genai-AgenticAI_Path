from flask import Flask,render_template,request,redirect,url_for
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method== 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method== 'POST':
#         name = request.form['name']
#         marks = request.form['marks']
#         return f"Hello {name}"
#     return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res="PASS"
    else: 
        res="FAIL"
    return render_template('result.html',results = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>=50:
        res="PASS"
    else: 
        res="FAIL"
    exp  = {'score':score,'res':res}
    return render_template('result1.html',results = exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results = score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        sst = float(request.form['sst'])
        english = float(request.form['english'])
        total_score = (science+maths+sst+english)/4
    else:
        return render_template('getresult.html')

    return redirect(url_for('successres',score = total_score))
if __name__ == '__main__':
    app.run(debug=True)