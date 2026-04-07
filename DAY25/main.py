import numpy as np
import pandas as pd

data = pd.read_csv("weather_data.csv")

print(type(data))           # <class 'pandas.core.frame.DataFrame'> — entire table
print(type(data['temp']))   # <class 'pandas.core.series.Series'> — single column

# convert dataframe to dictionary — keys are column names, values are dicts of {index: value}
data_dict = data.to_dict()
print(data_dict)

# convert a column to a plain Python list
print(data['temp'].to_list())

# numpy way to get average
average_temp = np.average(data['temp'])
print(average_temp)

# pandas built-in methods on a Series
average_with_pandas = data['temp'].mean()   # average
maximum_with_pandas = data['temp'].max()    # max value
print(average_with_pandas, maximum_with_pandas)

# two ways to access a column — dot notation and bracket notation
# dot notation only works if column name has no spaces and doesn't clash with pandas methods
print(data.condition)
print(data[data.day == "Monday"])  # filtering — returns all rows where day == "Monday"

# find the row with the highest temperature
highest_temp = data['temp'].max()                    # get the max value first
highest_temp_data = data[data.temp == highest_temp]  # filter rows where temp equals that max
print(highest_temp_data.condition)

# .iloc[0] gets first row by POSITION (always safe after filtering)
# ['temp'] then pulls the temp value from that row
# DO NOT use highest_temp_data.temp[0] — [0] refers to index LABEL not position
# after filtering, original index labels are preserved so [0] may not exist
highest_temp_c = highest_temp_data.iloc[0]['temp']
c_to_f = (highest_temp_c * 9/5) + 32
print(c_to_f)

# creating a DataFrame from scratch using a dictionary
# keys = column names, values = lists of data
data_dict = {
    "students": ['Amy', "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")  # saves to csv, adds an index column by default
                              # use to_csv("new_data.csv", index=False) to remove it