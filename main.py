from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hellog3g():
    return 'g3g is live'

@app.route('/open')
def openg3g():
    return 'building in progress'

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
   app.run()

