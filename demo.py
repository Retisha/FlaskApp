from flask import Flask

app = Flask(__name__)


@app.route('/demo')
def function1():
    return 'retisha'


if __name__ == '__main__':
    app.run()
