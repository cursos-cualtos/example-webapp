from flask import Flask, render_template
from utils import get_message
import os

app = Flask(__name__, static_url_path='')
port = int(os.getenv('PORT', 8000))

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

@app.route('/fruits/<id>')
def fruits(id):
    my_list = ['apples', 'oranges', 'grapes', 'pineapples', 'pears', 'watermelons']
    fruit = my_list[int(id):int(id) + 1]
    return render_template('listing.html', fruits=fruit)

@app.route('/messages')
def messages():
    message = get_message()
    return render_template('messages.html', message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)