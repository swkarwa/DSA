list = [1, 2, 3, 4, 5];

# inserting at last
list.append(6)
print(list)

# inserting at sepcific index
list.insert(1 , -1)
print(list)

# removing by value and index
list.remove(-1) # by value
print(list)
list.pop(1); # by index , if no index provided pop the last item from list
print(list)

# slice a list
new_list = list[1:4]
print(new_list)

## list comprehension
com_list = [x for x in range(0,10) if x%2==0] # create list
print(com_list)
com_lol = [[0 for _ in range(4)] for _ in range(3)] # create list in list
for l in com_lol:
    print(l)
print(com_lol)

# appendList
list.extend(com_list)
print(list)
# sort
list.sort()
print(list)

# forward iteration
for item in list:
    print(item , end="\t")

print()
# reverse iteration
for item in reversed(list):
    print(item , end = "\t")
print()
for i,item in enumerate(list):
    print(i ,"->", item , end="\t")

print()
# reverse for loop
for i in range(10 , -1 , -1):
    print(i , end="*")