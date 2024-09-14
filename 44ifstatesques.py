text=input("ENter the text\n")

if("buy now" in text):
    spam = True
elif("click this" in text):
    spam=True
elif("subscribe this" in text):
    spam =True
else:
    spam=False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")