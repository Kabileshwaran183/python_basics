
# with open('./Desktop/python programs documents/temp.csv') as file :
#     a = file.readlines()
#     print(a)

# import csv

# with open('./Desktop/python programs documents/temp.csv') as file :
#     data = csv.reader(file)
#     temp = []
#     for i in data:
#         if i[1] != 'temp':
#             temp.append(int(i[1]))
#     print(temp)

import pandas

data= pandas.read_csv('./Desktop/python programs documents/temp.csv')
print(data["temp"])
print(data.temp)
