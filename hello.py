#app.py 

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)