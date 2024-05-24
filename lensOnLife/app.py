from flask import Flask, render_template, redirect, url_for
from models import Era

app = Flask(__name__)

@app.route('/')
def index():
    eras = Era.query.all()
    return render_template('index.html', eras=eras)

if __name__ == '__main__':
    app.run(debug=True)
