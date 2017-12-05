import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path = '/etc/hosts'
redirect='127.0.0.1'
restricted_websites=["www.facebook.com","facebook.com","reddit.com","www.reddit.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        time.sleep(5)
        print("Get back to work!")
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in restricted_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in restricted_websites):
                    file.write(line)

            file.truncate()
        print("Get back to fun!")
    time.sleep(5)

# make sure path points to '/etc/hosts'
# to run this program:
# open crontab
#   * sudo nano crontab -e
# * then add:
#   * @reboot python3 /Users/hnefatafl/workspace/python/udemy/python-mega/website-blocker/blocker.py
