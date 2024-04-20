import calendar


def display_calendar(year, month):
    # Create a TextCalendar object
    cal = calendar.TextCalendar(calendar.SUNDAY)

    # Format the calendar for the given month and year
    calendar_text = cal.formatmonth(year, month)

    # Print the calendar
    print(calendar_text)


# Get user input for year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
display_calendar(year, month)

