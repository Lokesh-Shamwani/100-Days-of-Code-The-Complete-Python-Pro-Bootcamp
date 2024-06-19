from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap4
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        label="email", validators=[DataRequired(), Email("Invalid email address")]
    )
    password = PasswordField(
        label="password",
        validators=[
            DataRequired(),
            Length(8, 30, "Field must be at least 8 characters long."),
        ],
    )
    submit = SubmitField(label="Log In")


app = Flask(__name__)
bootstrap = Bootstrap4(app)
app.secret_key = "hastalavista"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
        
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
    
