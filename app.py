from flask import Flask
from controlllers.about import about_bp
from controlllers.home import home_bp
from controlllers.maps import maps_bp


app = Flask(__name__, template_folder = 'Templates')
app.register_blueprint(about_bp)
app.register_blueprint(home_bp)
app.register_blueprint(maps_bp)

if __name__== '__main__':
    app.run(debug=True)