from datetime import datetime
from flask import g

def prepare_data(f):
    def decorated_function(*args, **kwargs):
        g.total_weeks = 52 * 90  # Lifespan in weeks
        g.weeks_spent = 1129     # Weeks spent so far
        g.start_date = datetime.strptime("1984-01-01", "%Y-%m-%d")  # Birthdate
        g.end_date = datetime.now()  # Current date
        return f(*args, **kwargs)
    return decorated_function
