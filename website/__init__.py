from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sadfjkasjkd aslkfjslpf'
    app.config['TEMPLATES_AUTO_RELOAD']=True
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_perfix = "/")
    return app
config= { "DEBUG": True }
app =Flask(__name__)
app.config.from_mapping(config)