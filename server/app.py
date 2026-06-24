
from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Username route
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run the application
if __name__ == '__main__':
    app.run(port=5555, debug=True)



