"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and year % 4 == 0:
        return days[month] + 1
    else:
        return days[month]


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR and \
            1 <= month <= month <= 12 and \
            1 <= day <= days_in_month(year, month):
        return True
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        earlier_date = datetime.date(year1, month1, day1)
        later_date = datetime.date(year2, month2, day2)

        if later_date > earlier_date:
            return (later_date - earlier_date).days
        else:
            return 0
    else:
        return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day):
        today = datetime.date.today()
        return days_between(year, month, day, today.year, today.month, today.day)
    else:
        return 0

# Testing
# days_in_month(2021, 2)
# days_in_month(2020, 2)
# days_in_month(2024, 2)
# days_in_month(2022, 3)
# days_in_month(2023, 5)
# days_in_month(2024, 6)
#
# is_valid_date(2021, 9, 32)
# is_valid_date(2030, 2, 29)
# is_valid_date(2030, 2, 28)
# is_valid_date(2030, 12, 31)

# days_between(2020, 2, 30, 2021, 2, 28)
# age_in_days(1984, 9, 17)