arr=["aeroplane","aeircraft","aero"]
i=0
letter=""
eql_letter=""
flag=True
for i in range(len(arr[0])): #length of the 1st element in array. (9)(aeroplane)
    check_letter=arr[0][i] # check all letters one by one ( a e r o p l a n e )
    j=0
    while j < len(arr) and flag:
        if i<len(arr[j]):
            if arr[j][i] == check_letter :
                letter=check_letter
            else:
                letter=""
                flag=False
        else:
            letter=""
            flag=False
        j+=1
    eql_letter+=letter
print(eql_letter)
            


# while i<len(arr) and flag:
#     for j in range (len(arr[i])):
#         check_letter = arr[i][j]
#         if j==0:
#             letter += check_letter
#         if letter == check_letter:
#             break
#         else:
#             flag=False
#     i+=1



