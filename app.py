from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    file = open('Timestamp.txt', 'a')
    file.write(str(datetime.now()) + '\n')
    return "Hello World!!!!!"


if __name__ == "__main__":
    print(2)
    app.run()