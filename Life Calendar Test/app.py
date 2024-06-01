from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data representing weeks lived and total weeks
total_weeks = 52 * 90  # 90 years, as from your 'calendar' route
weeks_spent = 1129  # Example data

# Define the lenses
lenses = {
    "default": {"name": "Default View", "color": "#90EE90"},
    "highlights": {"name": "Life Highlights", "color": "#FFD700"},
    "challenges": {"name": "Challenges", "color": "#FF6347"}
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    current_lens = 'default'
    if request.method == 'POST':
        current_lens = request.form.get('lens_selector')

    # Get the color based on the selected lens
    color = lenses.get(current_lens, lenses['default'])['color']

    return render_template('calendar.html', total_weeks=total_weeks, weeks_spent=weeks_spent,
                           percentage=round((weeks_spent / total_weeks) * 100, 1),
                           lenses=lenses, current_lens=current_lens, color=color)


if __name__ == "__main__":
    app.run(debug=True)
