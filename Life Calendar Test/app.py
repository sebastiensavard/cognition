from flask import Flask, render_template, request, redirect, url_for
from utils import prepare_data

app = Flask(__name__)

# Define the lenses with specific event periods
lenses = {
    "default": {"name": "Default View", "color": "#90EE90"},
    "university": {
        "name": "Went to university 2002-2006",
        "color": "#FFD700",
        "start_date": "2002-01-01",
        "end_date": "2006-12-31"
    }
}

@app.route('/', methods=['GET', 'POST'])
@prepare_data
def index():
    return render_template('index.html', lenses=lenses)

@app.route('/calendar', methods=['GET', 'POST'])
@prepare_data
def calendar():
    current_lens = request.form.get('lens_selector', 'default')
    return render_template('calendar.html', current_lens=current_lens, lenses=lenses)

if __name__ == "__main__":
    app.run(debug=True)
