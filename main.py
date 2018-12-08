from flask import Flask

#Set the root path
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the Homepage'

if __name__ == '__main__':
    app.run(debug=True)
