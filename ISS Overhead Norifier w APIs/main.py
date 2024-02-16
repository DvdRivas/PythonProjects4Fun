import requests
import datetime
import smtplib
import time
LOCAL_UTC_OFFSET = -7
MY_LAT = ####
MY_LONG = ####
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
my_email = "example@gmail.com"
password = "gmail token"
def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour
#=============== ASK FOR THE TIME OF SUNSET AND SUNRISE =================
petition = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
petition.raise_for_status()
SUNRISE = int(petition.json()["results"]["sunrise"].split("T")[1].split(":")[0])
SUNSET = int(petition.json()["results"]["sunset"].split("T")[1].split(":")[0])
LT_SUNRISE = utc_to_local(SUNRISE)
LT_SUNSET = utc_to_local(SUNSET)

def asking():
#=========== ASK FOR THE CURRENT POSITION OF THE ISS =================
    def check():
        if MY_LAT - 5 <= lat <= MY_LAT + 5 and MY_LONG - 5 <= long <= MY_LONG + 5:
            return True
        else:
            return False

    position = requests.get(url="http://api.open-notify.org/iss-now.json")
    position.raise_for_status()
    lat = float(position.json()["iss_position"]["latitude"])
    long = float(position.json()["iss_position"]["longitude"])
    if (datetime.datetime.now().hour > LT_SUNSET or datetime.datetime.now().hour < LT_SUNRISE) and check():
        print("Send!")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="example.com",
                            msg="Subject:Look Up!\n\n"
                                "The international station is now above you")
        connection.close()
    else:
        print("None")
# asking()
while True:
    asking()
    time.sleep(60)
