from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecret!'
Bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[InputRequired(),
                                                   Length(min = 4, max = 8, message='Must be between 4 and 8 characters')])
    password = PasswordField('password', validators=[InputRequired()])
    age = IntegerField('age')
    true = BooleanField('true')
    email = StringField('email', validators=[Email()])


class User:
    def __init__(self, username, age, email):
        self.username = username
        self.age = age
        self.email = email


@app.route('/', methods =['GET', 'POST'])
def index():
    myuser = User('lazaro', 27, 'lrcamacho@uci.com')

    form = LoginForm(obj=myuser)
    if form.validate_on_submit():
        return '<h1>User: {}, Password: {}'.format(form.username.data, form.password.data)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)