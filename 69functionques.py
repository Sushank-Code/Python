def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this ="   Harry is good     "
n=remove_and_split(this,"Harry")
print(n)

# WAP to remove a word from string and strip it.