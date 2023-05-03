import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:

    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users 
            (username, email, password)
            VALUES (%(username)s,%(email)s,%(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_by_email(cls, data):
        query = """
            SELECT * FROM users WHERE email  = %(email)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result)<1:
            return False
        return cls(result[0])

        
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['username'])<2:
            is_valid = False
            flash("Username must be at least 2")
        if not EMAIL_REGEX.match(data['email']): 
            is_valid = False
            flash("Email not valid")
        elif User.get_by_email({'email':data['email']}):
            is_valid = False
            flash("Email Already Exist")
        if len(data['password'])<6:
            is_valid = False
            flash("Password greater than 6")
        elif data['password']!= data['confirm_password']:
            is_valid = False
            flash("Password and Confirm password must match")
        return is_valid