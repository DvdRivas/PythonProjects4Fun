import requests
import datetime
TOKEN = " "
USERNAME = "user"
# ===================== Create the account in Pixela ============================
# params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# res = requests.post(url="https://pixe.la/v1/users",json=params)
# print(res.text)
# ===================== Create a Graph ===============================
# g_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
# conf = {
#     "id": "graph1",
#     "name": "Kilometers Graph",
#     "unit":"Km",
#     "type": "float",
#     "color": "ajisai"
# }
header = {
    "X-USER-TOKEN":TOKEN
}
# requests.post(url=g_endpoint,headers=header,json=conf)

# =========================== Set pints ===================
post = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

#Get the current day
# year = str(datetime.datetime.now().year)
# month = "0"
# if datetime.datetime.now().month < 10:
#     month += str(datetime.datetime.now().month)
# else:
#     month = str(datetime.datetime.now().month)
# day = "0"
# if datetime.datetime.now().day < 10:
#     day += str(datetime.datetime.now().day)
# else:
#     day = str(datetime.datetime.now().day)

# Optimized:

# data = {
#     "date": "20230730",#datetime.datetime.now().strftime("%Y%m%d"), #Exactly the same of above
#     "quantity": "2"
# }

# ans = requests.post(url=post,headers=header,json=data)
# print(ans)

# Updating a pixel
date = "20230730"
# data = {
#     "quantity": "2"
# }
# ans = requests.put(url=f"{post}/{date}",headers=header,json=data)
# print(ans)

# Deleting a pixel
ans = requests.delete(url=f"{post}/{date}",headers=header)
print(ans)