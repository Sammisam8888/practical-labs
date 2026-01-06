
from flask import Flask
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = 'devkey'
    with app.app_context():
        from . import routes
    return app
app = create_app()
