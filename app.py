from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, coffee lovers!"

@app.route('/menu')
def menu():
    return "Here is what we offer at our coffee shop!"

@app.route('/contact')
def contact():
    return "Have questions? Reach out to us here!"

if __name__ == '__main__':
    app.run(debug=True)