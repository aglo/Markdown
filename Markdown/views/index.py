from Markdown import app

@app.route('/')
def hello_world():
    print 'Arcma'
    return 'Hello World!'
