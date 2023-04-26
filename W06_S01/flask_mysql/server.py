from flask import Flask , render_template, request, redirect
from singer_model import Singer
app = Flask(__name__)

@app.route('/')
def index():
    singers_list = Singer.get_all()
    return render_template("index.html", singers_list = singers_list)


if __name__ =='__main__':
    app.run(debug = True, port = 5001)