from flask_app import app

# ! Don't Forget To Import All* controllers (Routes)
from flask_app.controllers import users, parties

if __name__ =='__main__':
    app.run(debug=True, port=5001)