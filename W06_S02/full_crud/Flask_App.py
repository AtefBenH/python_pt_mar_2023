# Create a FlaskApp
"""
1  Create an empty folder
2 cd folder_name
3 pipenv install flask pymysql
4 pipenv shell
5 code .
6 server.py 
7 inside server.py (
    from flask import Flask , render_template, request, redirect
    from singer_model import Singer
    app = Flask(__name__)

    if __name__ =='__main__':
        app.run(debug = True, port = 5001)
    )
8 Add Routes to server.py
"""