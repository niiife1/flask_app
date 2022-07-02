from cgitb import html
from distutils.command.config import config
from website import create_app
from flask import Flask
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)