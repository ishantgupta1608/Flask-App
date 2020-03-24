from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    file = open('Timestamp.txt', 'a')
    file.write(str(datetime.now()) +':' +  '\n')
    file.close()
    return open('Timestamp.txt', 'r').read()


if __name__ == "__main__":
    #print(2)
    app.run(debug = True)
