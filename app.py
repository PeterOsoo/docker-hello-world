from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_docker():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello again, from my updated containerized Python app!</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
