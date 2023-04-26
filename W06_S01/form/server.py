from flask import Flask , render_template, request, redirect,session

app = Flask(__name__)
app.secret_key = 'no secrets on GitHUB'
# ? RENDER THE PAGE - FROM 👀
@app.route('/')
def index():
    return render_template("index.html")

# ? ACTION ROUTE - FROM SUBMIT (POST) 📤📤
@app.route('/process', methods=['post'])
def process():
    print("Request Object ", request.form, "*"*25)
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['favorite_food'] = request.form['favorite_food']
    """
        return render_template("display.html", name = request.form['name'],
        age = request.form['age'],
        favorite_food = request.form['favorite_food'])
    """
    return redirect('/display')

# ? ROUTE PAGE - DISPLAY 👀
@app.route('/display')
def display():
    # print("Username : ", session['name'],"-"*25)
    return render_template("display.html")

# ? ACTION ROUTE - CLEAR SESSION 🧹
@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')

if __name__ =='__main__':
    app.run(debug = True, port = 5001)