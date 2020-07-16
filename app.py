from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/variables')
def variables():
    my_number = 23
    message = 'Hello'
    my_decimal = 3.24
    return render_template('variables.html', my_number=my_number, message=message, my_decimal=my_decimal)

@app.route('/listing')
def listing():
    my_list = ['apples', 'oranges', 'grapes', 'pineapples', 'pears', 'watermelons']
    return render_template('listing.html', fruits=my_list)