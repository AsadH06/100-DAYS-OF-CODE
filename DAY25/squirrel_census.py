import pandas as pd
import numpy as np

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

data_color = data['Primary Fur Color']
data_count = data_color.value_counts()
print(data_count)
data_count.to_csv("squirrel_data.csv")

# data_dict = {
#     'Gray': data_list['Gray'].count(),
#     'Cinnamon': data_list['Cinnamon'].count(),
#     'Black': data_list['Black'].count()
# }
# data_to_df = pd.DataFrame(data_dict)
# data_to_df.to_csv("squirrel_data.csv")