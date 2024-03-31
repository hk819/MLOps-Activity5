from flask import Flask, request

app = Flask(__name__)

# MongoDB connection setup
from pymongo import MongoClient
client = MongoClient('mongodb://mongo:27017/')
db = client['webapp']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Inserting data into MongoDB
    collection.insert_one({'name': name, 'email': email})
    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')