import requests
from datetime import datetime
import smtplib
import time

my_email = "yourmail@gmail.com"
password = "your_pass"

MY_LAT = 41.299496
MY_LONG = 69.240074
GMT = +5

# ############# Position of International Space Station ##################
response = requests.get(url="http://api.open-notify.org/iss-now.json")   #
response.raise_for_status()                                              #
data = response.json()                                                   #

iss_longitude = float(data["iss_position"]["longitude"])                 #
iss_latitude = float(data["iss_position"]["latitude"])                   #
##########################################################################

# ########################## Sunrise and Sunset time  ##################################
parameters = {                                                                         #
    "lat": MY_LAT,                                                                     #
    "lng": MY_LONG,                                                                    #
    "formatted": 0                                                                     #
}                                                                                      #

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)  #
response.raise_for_status()                                                            #
data = response.json()                                                                 #
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + GMT            #
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + GMT              #
# ######################################################################################
time_now = datetime.now().hour

while True:
    time.sleep(60)
    if 5 >= iss_latitude - MY_LAT >= -5 and 5 >= iss_longitude - MY_LONG >= -5:
        if sunrise >= time_now >= sunset:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="any_mail@gmail.com",
                    msg=f"Subject:Look up👆\n\nHurry up!\nThere is an ISS (International Space Station) in the sky. "
                        f"It's just above you. "
                )
