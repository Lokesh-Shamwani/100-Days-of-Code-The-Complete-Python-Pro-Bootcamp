import datetime as dt
import random
import pandas
import smtplib

MY_EMAIL = "YOUR EMAIL GOES HERE"
MY_PASSWORD = "YOUR APP PASSWORD GOES HERE"


# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.day, now.month)

bdy_data = pandas.read_csv("birthdays.csv")  # DATAFRAME
bdy_dict = {
    (data_row["day"], data_row["month"]): data_row
    for (index, data_row) in bdy_data.iterrows()
}

for entry in bdy_dict:
    if today == entry:
        recipents_data = bdy_dict[entry]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            content = file.read()
            letter_to_send = content.replace("[NAME]", recipents_data["name"])

        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipents_data["email"],
                msg=f"Subject: Happy Birthday wish tester\n\n{letter_to_send}",
            )
