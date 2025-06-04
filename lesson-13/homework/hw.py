age calculator
import datetime

date_str = input("Enter your birthday (yyyy-mm-dd): ")
birth_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

today = datetime.date.today()

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Your age is:", age)

import datetime
date_str = input("Enter your birthday (yyyy-mm-dd): ")
birth_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
today = datetime.date.today()
this_year_birthday = birth_date.replace(year=today.year)
if this_year_birthday < today:
    this_year_birthday = this_year_birthday.replace(year=today.year + 1)

days_until = (this_year_birthday - today).days
print(f"Days until your next birthday: {days_until}")

from datetime import datetime
start = input('enter current date and time (yyyy-mm-dd, hh-mm): ')
end = input('enter when meeting ends: ')

y = datetime.strptime(start, "%Y-%m-%d, %H-%M")

end_time = datetime.strptime(end, "%H-%M")
end_time = end_time.replace(year=y.year, month=y.month, day=y.day)
delta = end_time - y
hours = delta.total_seconds() // 3600
minutes = (delta.total_seconds() % 3600) // 60

print(f"Meeting duration: {int(hours)} hours and {int(minutes)} minutes")
import pytz
from datetime import datetime
a = input('enter a timezone wou want (Continent/City): ')
try:
    tmz = pytz.timezone(a)
    x = datetime.now(tmz)
    print("Time in", a, "is:", x.strftime('%H:%M:%S'))
except pytz.UnknownTimeZoneError:
    print("Invalid timezone. Please use format like 'Asia/Tashkent' or 'Europe/Moscow'")
import time
from datetime import datetime

def countdown_timer():
    user_input = input("Enter a future date and time (format: YYYY-MM-DD HH:MM:SS): ")
    try:
        target_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid format. Please try again.")
        return

    while True:
        now = datetime.now()
        time_left = target_time - now

        if time_left.total_seconds() <= 0:
            print("\n⏰ Time's up!")
            break
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"\rTime remaining: {days}d {hours:02d}h {minutes:02d}m {seconds:02d}s", end="")
        time.sleep(1)

countdown_timer()

import re

def validate_email():
    email = input("Enter an email address to validate: ")

    # Regular expression for a basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        print("✅ Valid email address.")
    else:
        print("❌ Invalid email address.")

# Run the validator
validate_email()

def format_phone_number():
    raw_input = input("Enter a 10-digit phone number (numbers only): ")

    # Remove any non-digit characters just in case
    digits = ''.join(filter(str.isdigit, raw_input))

    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print("Formatted phone number:", formatted)
    else:
        print("❌ Invalid input. Please enter exactly 10 digits.")

# Run the function
format_phone_number()

def check_password_strength():
    password = input("Enter a password to check its strength: ")

    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)

    if length_ok and has_upper and has_lower and has_digit:
        print("✅ Strong password.")
    else:
        print("❌ Weak password. Your password must:")
        if not length_ok:
            print("- Be at least 8 characters long")
        if not has_upper:
            print("- Contain at least one uppercase letter (A–Z)")
        if not has_lower:
            print("- Contain at least one lowercase letter (a–z)")
        if not has_digit:
            print("- Contain at least one digit (0–9)")

# Run the checker
check_password_strength()

