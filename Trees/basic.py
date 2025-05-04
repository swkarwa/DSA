for i in range(1,6):
    print('*'*i)


result = [[0 if row%2 ==0 else 1 for c in range(5)]for row in range(4)]
print(result)

l = [0,1,2,3,4,5]
left = 0
right = len(l)-1
while(left <= right):
    l[left] , l[right] = l[right] , l[left]
    left+=1
    right-=1
print(l)