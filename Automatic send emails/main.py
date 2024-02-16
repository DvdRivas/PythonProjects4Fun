import smtplib
import datetime as dt
from random import choice
with open ("quotes.txt","r") as data:
    list_of_quotes = data.readlines()

my_email = "example@gmail.com"
password = "api key"
now = dt.datetime.now()
day = now.strftime("%A")
if day == "Thursday" and now.hour == 20:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="example@hotmail.com",
                        msg="Subject:It's Friday!\n\n"
                            f"{choice(list_of_quotes)}")
    connection.close()

# birthday = dt.datetime(year=1999, month=8, day=17,hour=12)
