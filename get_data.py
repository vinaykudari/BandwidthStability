import speedtest
import datetime
from tinydb import TinyDB

time = datetime.datetime.now()
db = TinyDB('bandwidth_data.json')

month = int(time.month)
day = int(time.day)
hour = int(time.strftime("%H")) + 1                             #To avoid 0
weekday = int(time.weekday()) + 1
server = [12353]                                                #Best server for BSNL Kolkata Region
download_speed = 0

s = speedtest.Speedtest()
s.get_servers(server)
s.get_best_server()

for i in range(0,3):                                            #Averaging to get optimum bandwidth
    download_speed += s.download()

download_speed = download_speed/3

db.insert({'month':month,"day":day,"weekday":weekday,"hour":hour,"download_speed":download_speed})



