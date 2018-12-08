from flask import Flask, request

#Set the root path
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the Homepage'

@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probably using GET'

# @app.route('/tuna')
# def tuna():
#     return '<h2>Tuna is Good</h2>'
#
# @app.route('/profile/<username>')
# def profile(username):
#     return '<h1>Hello {}!'.format(username)
#
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     return '<h1>Hello {}!'.format(post_id)

if __name__ == '__main__':
    app.run(debug=True)
