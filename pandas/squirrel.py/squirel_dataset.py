import pandas

data = pandas.read_csv('./Desktop/python programs documents/Squirrel_Data.csv')
# total_gray_squirel = len(data[data["Primary Fur Color"]== "Gray"])
# total_cinnamon_squirel = len(data[data["Primary Fur Color"]== "Cinnamon"])
# print(total_gray_squirel)
# print(total_cinnamon_squirel)

list_color = ["Gray","Black","Cinnamon"]
count = []

for i in list_color :
    total_color = len(data[data["Primary Fur Color"]== i])
    count.append(total_color)
    print(total_color)

dict_1 = {
    "fur color" : ["Gray","Black","Cinnamon"],
    "count" : [count[0],count[1],count[2]]
}

df = pandas.DataFrame(dict_1)
df.to_csv("./Desktop/python programs documents/squirrel_count.csv")