from flask import Flask

#Set the root path
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the Homepage'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is Good</h2>'

@app.route('/profile/<username>')
def profile(username):
    return '<h1>Hello {}!'.format(username)

if __name__ == '__main__':
    app.run(debug=True)
