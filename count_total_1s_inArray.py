arr=[1,1,0,1,1,1,0]
count=0
i=0
max_count=0
while i<len(arr)-1:
    if arr[i]==1:
        count+=1
    else :
        if max_count<count:
            max_count=count
        count = 0
    i+=1
print(max_count)
        


