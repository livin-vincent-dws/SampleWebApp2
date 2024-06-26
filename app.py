from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask Web App!</h1>"

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'name': 'Flask',
        'version': '1.0',
        'description': 'A simple Flask web application 12345'
    }
    return jsonify(sample_data)

# New route for the form
@app.route('/form', methods=['GET'])
def form():
    form_html = '''
    <form action="/submit" method="POST">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
    '''
    return render_template_string(form_html)

# New route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return redirect(url_for('greet', name=name))

# New route to display the greeting
@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
