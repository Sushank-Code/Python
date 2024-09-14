col={
    "fast":"In a quick manner",
    "sushank":"Gamer",
    "marks":[1,45,2],
    "num":(34,56,566),
    "Ancol":{'hey':'What'},
    1:4
}
#print(tuple(col.keys()))
#print(list(col.values()))
#print(list(col.items()))   
 
'''col2={
    "happy":"sad"   #same as below of using update method
}
col.update(col2)
print(col)'''

print(col)
col.update({"happy":"sad",
             "hello":"hi",
             1:5})
print(col)

print(col.get(input("Enter the keys")))
