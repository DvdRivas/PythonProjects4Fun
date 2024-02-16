import requests
import os
from twilio.rest import Client
API_KEY = " "
MY_LAT = XXXX
MY_LONG = XXXX
LOCAL_UTC_OFFSET = -7
account_sid = " "
auth_token = " "

#=======================================================================================
wheater = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&exclude=daily&appid=69f04e4613056b159c2761a9d9e664d2")#One Call Func
wheater.raise_for_status()
wheater_data = wheater.json()
wheater_list = [state["weather"][0]["description"] for state in wheater_data["hourly"][:12]]
string = f"El pronostico para las siguientes horas es: \n" \
         f"8:00: {wheater_list[0]}\n" \
         f"9:00: {wheater_list[1]}\n" \
         f"10:00: {wheater_list[2]}\n" \
         f"11:00: {wheater_list[3]}\n" \
         f"12:00: {wheater_list[4]}\n" \
         f"13:00: {wheater_list[5]}\n" \
         f"14:00: {wheater_list[6]}\n" \
         f"15:00: {wheater_list[7]}\n" \
         f"16:00: {wheater_list[8]}\n" \
         f"17:00: {wheater_list[9]}\n" \
         f"18:00: {wheater_list[10]}\n" \
         f"19:00: {wheater_list[11]}\n"

client = Client(account_sid, auth_token)
message = client.messages \
        .create(
        body=string,
        from_='number',
        to='reciber'
    )
print(message.status)


