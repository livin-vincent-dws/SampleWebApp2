from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask Web App!</h1>"

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'name': 'Flask',
        'version': '1.0',
        'description': 'A simple Flask web application'
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
