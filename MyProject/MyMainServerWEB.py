from flask import Flask

app = Flask(__name__)

@app.route('/login')
def login():
    return 'Hello, welcome!'

@app.route('/login/<name>')
def private_login(name):
    return 'Hello ' + name + '!'

def main():
    app.run(host='0.0.0.0',port=80)

if __name__ == '__main__':
    main()