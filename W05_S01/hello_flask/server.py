from flask import Flask, render_template

# Class Flask
# print("__name__ Value = ",__name__)
app = Flask(__name__)

# http://127.0.0.1:5000
# localhost:5000

# localhost:5000/
@app.route('/')
def hello_world():
    return "Hello World !!!"


@app.route('/hello')
def hello():
    return "Hello"

@app.route('/hello/<name>')
def hello_name(name):
    print("*"*25,name,"*"*25)
    return f"Hello {name} !!!!"

@app.route('/hello/hello/alert/<name>')
def hello_alert_name(name):
    print("*"*25,name,"*"*25)
    return f"<h1>Hello {name} !!!!</h1><script>alert('We Got You')</script>"

@app.route('/hello/<name>/<int:times>')
def hello_times(name,times):
    print(f"Name : {name}\nTimes : {times}")
    return f"Hello {name} <br/>" *times


# @app.route('/hello/<name>/<times>')
# def hello_times(name,times):
#     print(f"Name : {name}\nTimes : {times}")
#     return f"Hello {name}<br/>" *int(times)

@app.route('/index')
def index():
    return render_template("index.html", x = 200)

@app.route('/index/<name>')
def index_name(name):
    return render_template("index.html", name = name, x = 5)

if __name__ == "__main__":
    app.run(debug=True, port=5003)
