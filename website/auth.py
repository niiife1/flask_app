from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template("login.html", text="testing", boolean=True)

@auth.route('/logout')
def logout():
    return("<p>Logout</p>")

@auth.route('/sing-up')
def sing_up():
    return render_template("sing_up.html")