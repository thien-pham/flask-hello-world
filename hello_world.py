from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<name>/<last>")
def jedi(name, last):
    return "Your Jedi name is {}{}".format(last[:3], name[:2])

# if __name__ == "__main__":
#     app.run(host=environ['IP'],
#             port=int(environ['PORT']))

if __name__ == '__main__':
	app.run()  # Run our application

# from flask import Flask
# from home.views import home_view
#
# def create_app(config_file):
# 	app = Flask(__name__)  # Create application object
# 	app.config.from_pyfile(config_file)  # Configure application with settings file, not strictly necessary
# 	app.register_blueprint(home_view)  # Register url's so application knows what to do
# 	return app
#
# if __name__ == '__main__':
# 	app = create_app('settingslocal.py')  # Create application with our config file
# 	app.run()  # Run our application
# <br>
