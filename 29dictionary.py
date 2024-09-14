col={
    "fast":"In a quick manner",
    "sushank":"Gamer",
    "marks":[1,45,2],
    "num":(34,56,566),
    "Ancol":{'hey':'What'}
}
print(col["sushank"])
col["marks"]=[45,78]
print(col["marks"])
print(col["num"])
#print(col["Ancol"]['hey'])
print("\n")
for key ,value in col.items():
    print(f"{key}:{value}")

