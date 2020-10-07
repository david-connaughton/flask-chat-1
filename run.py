import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello There!</h1>"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            debug=True)
