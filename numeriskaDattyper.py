import datetime
now = datetime.datetime.now()


timeH = now.hour
timeM = now.minute
googol = 10


for i in range (googol):
    timeM = timeM +1
    if timeM > 60:
        timeM = 0
        timeH = timeH +1
    if timeH > 24:
        timeH = 0 
    realtime = (timeH , timeM)
    
print(realtime)

