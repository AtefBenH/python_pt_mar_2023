from flask_app import app
# ! Don't Forget to import All Controllers Here
from flask_app.controllers import singers_controllers


if __name__ =='__main__':
    app.run(debug = True, port = 5001)


