from flask_app import app
from flask_app.models.user import User
from flask import request , redirect, session, render_template, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# ========================INDEX PAGE=================

@app.route('/')
def index():
    return render_template("index.html")

#  =======================REGISTER===================

@app.route('/users/create', methods=['post'])
def register():
    if User.validate(request.form):
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        print(hashed_password)
        # 11111111 === b'$2b$12$Lzolv2rNQQmRaVvAs7IxTuDV/9177Vl3x0Y4dn9nFwTV4kd1KIFQi'
        data = {
            'username':request.form['username'],
            'email':request.form['email'],
            'password':hashed_password,
        }
        data = {
            **request.form, 'password':hashed_password
        }
        user_id = User.create(data)
        session['user_id'] = user_id
        # user_id in session (7) ==== eyJ1c2VyX2lkIjoxMH0.ZFFq7w.gRS7V6gBpbUysUBbZlvnpsnQIyg
        # session['user_id'] = User.create(data)
        return redirect('/dashboard')
    return redirect('/')


# ===========================DASHBOARD==================
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("dashboard.html")

# ===============================LOGIN===================

@app.route('/users/login', methods = ['post'])
def login():
    # Verify the email : if the email exist
    print(request.form, '*'*25)
    user_form_db = User.get_by_email({'email':request.form['email']})
    if user_form_db:
        # YES exist
        # Check the Password
        if not bcrypt.check_password_hash(user_form_db.password, request.form['password']):
            flash("Invalid Email/Password")
            return redirect('/')
        else :
            session['user_id'] = user_form_db.id
            return redirect ('/dashboard')
    flash("Invalid Email/Password")
    return redirect('/')


# ==========================LOGOUT==============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')