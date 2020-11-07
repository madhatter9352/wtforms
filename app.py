from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecret!'


if __name__ == '__main__':
    app.run(debug=True)