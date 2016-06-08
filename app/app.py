from flask import Flask, render_template, g

app = Flask(__name__)

@app.route('/')
def home():
    g.path = '/'
    return render_template('home.html')


if __name__ == '__main__':
    app.run()