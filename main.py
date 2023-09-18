from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellog3g():
    return 'g3g is live'

@app.route('/open')
def openg3g():
    return 'building in progress'

if __name__ == '__main__':
   app.run()

