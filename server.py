from flask import Flask, render_template

def page_not_found():
    return render_template('404.html'), 404

app = Flask(__name__)
app.register_error_handler(404, page_not_found)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/two')
def two():
    return str(2)

# TODO: Find something for the unit tests...

app.run()