import time
hour = int(time.strftime('%H'))

if(hour>=0 and hour<12):
    print("Good morning sir")
elif(hour>=12 and hour<=17):
    print("Good Afternoon sir")
else:
    print("Good night sir")

'''import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)'''