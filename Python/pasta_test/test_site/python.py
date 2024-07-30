from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password'] 

    if username == 'admin' and password == 'admin':
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
    return 'Welcome!'

if __name__ == '__main__':
    app.run(debug=True)
