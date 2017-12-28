import speedtest
import datetime
from tinydb import TinyDB,Query

time = datetime.datetime.now()
db = TinyDB('bandwidth_data.json')

month = time.month
day = time.day
hour = time.strftime("%H")
weekday = time.weekday()
server = [12353]
download_speed = 0

print(month)
print(day)
print(hour+1)
print(weekday)

s = speedtest.Speedtest()
s.get_servers(server)
s.get_best_server()

for i in range(0,3):
    download_speed += s.download()
    print(download_speed)

download_speed = download_speed/3
