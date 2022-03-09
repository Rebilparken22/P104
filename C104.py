from statistics import median_high
import pandas as pd
import plotly.figure_factory as ff


df = pd.read_csv("HeightWeight.csv")
list_height = df["Height"].tolist()

result = 0
for i in list_height:
    result += i
print(result)

mean = result/len(list_height)
# print("mean Of Heights",mean)

list_weight = df["Weight"].tolist()

result = 0
for x in list_weight:
    result += x
print(result)

meanw = result/len(list_weight)
# print("mean of weights",meanw)

fig = ff.create_distplot([list_height],["heights"])
# fig.show()

# list_height = list_height.sort()
# length = len(list_height)
# median = list_height[length/2]
print(list_height.sort())