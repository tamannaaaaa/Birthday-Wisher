import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "pythondeveloper23072001@gmail.com"
MY_PASSWORD = "python@23"

today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# The iterrows() method generates an iterator object of the DataFrame, allowing us to iterate each row in the DataFrame.
#
# Each iteration produces an index object and a row object (a Pandas Series object).
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:\n\n{contents}")