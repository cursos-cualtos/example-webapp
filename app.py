from flask import Flask, render_template
from utils import get_message
import os
from cloudant.client import Cloudant
import atexit


app = Flask(__name__, static_url_path='')
port = int(os.getenv('PORT', 8000))

username = 'fe8f30e8-02b6-4aae-8420-0b97d69fc6bf-bluemix'
password = 'a89179453442149233f950791d9feda2f168a9d59d774028ee64bbcdf06435bc'
url = 'https://fe8f30e8-02b6-4aae-8420-0b97d69fc6bf-bluemix.cloudant.com'

client = Cloudant(username, password, url=url, connect=True)
#my_database = client.create_database('my_database')
my_database = client['my_database']
if my_database.exists():
    pass
elif not my_database.exists():
    my_database = client.create_database('my_database')
else: 
    print("error")
    
global_val = 'Hello'

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

@app.route('/test')
def test():
    data = {
        'message': 'Hello World'
    }
    my_document = my_database.create_document(data)
    if my_document.exists():
        return str(my_document)
    else:
        return 'Error'

@atexit.register
def shutdown():
   client.disconnect()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)