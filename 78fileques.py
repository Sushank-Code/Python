# Attempt 77fileques but replace "####" with different names this time in same existing file.

words=["donkey","mote","fool"]

with open("sample78ques.txt","r") as f:
    data = f.read() 

for item in words:
    data=data.replace(item,"#####")
    with open("sample78ques.txt","w") as f:
         f.write(data)