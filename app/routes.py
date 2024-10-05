from app import app

# these are decorators to the index function
@app.route('/')
@app.route('/index')
def index():
    return "Hello World from my Flask app!"