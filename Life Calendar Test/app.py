from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    weeks = 52 * 90  # Assuming a lifespan of 90 years
    return render_template('calendar.html', weeks=weeks)

if __name__ == '__main__':
    app.run(debug=True)
