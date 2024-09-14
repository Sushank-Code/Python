a=set()
a.add(1)
a.add((1,2,3,4))
a.add(4)
print(a)

print(len(a))

# a.remove(1)     # Removes an element
# print(a)

# a.pop()         # Removes the random element  
# print(a)

# a.clear()        # Clear all element
# print(a)

b=a.union({1,7,4,5,8})
print(b)

c=a.intersection({4,1})
print(c)