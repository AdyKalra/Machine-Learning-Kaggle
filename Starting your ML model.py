import pandas as pd

# save filepath to variable for easier access
main_file_path = '../input/train.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(main_file_path)

# print a summary of the data in Melbourne data
print(melbourne_data.describe())

# print all columns 
print(melbourne_data.columns)

# store the series of prices separately as melbourne_yearbuilt_data.
melbourne_yearbuilt_data = melbourne_data.YearBuilt

# the head command returns the top few lines of data.
print(melbourne_yearbuilt_data.head())
