import sys
import pandas as pd
from fontTools.misc.textTools import caselessSort
from numpy.ma.core import argmin, argmax

data = pd.read_csv('us-counties.csv')

rockingham_data = data[(data['fips'] == 51165.0) & (data['cases'] > 0)] # checking to see if cases > 0 is redundant

first_rockingham_case = rockingham_data.iloc[0, 0] # select the value from the 0th row and 0th column

print("The first positive case in Rockingham occurred on: " + str(first_rockingham_case))

harrisonburg_data = data[(data['county'] == 'Harrisonburg city') & (data['cases'] > 0)]

first_harrisonburg_case = harrisonburg_data.iloc[0, 0]

print("The first positive case in Harrisonburg city occurred on: " + str(first_harrisonburg_case))

rockingham_data_array = rockingham_data.to_numpy()

rockingham_list = list() # create list to store
for i in range(1,len(rockingham_data_array)):
    current_max = rockingham_data_array[i,4] - rockingham_data_array[i-1,4]
    rockingham_list.append(current_max)

rockingham_index = argmax(rockingham_list)
worst_rockingham_cases_date = rockingham_data_array[rockingham_index,0]
print("The worst day for new reported cases in Rockingham county is "+ worst_rockingham_cases_date)

harrisonburg_data_array = harrisonburg_data.to_numpy()

harrisonburg_list = list()
for i in range(1,len(harrisonburg_data_array)):
    current_max = harrisonburg_data_array[i,4] - harrisonburg_data_array[i-1,4]
    harrisonburg_list.append(current_max)

harrisonburg_index = argmax(harrisonburg_list)
worst_harrisonburg_cases_date = harrisonburg_data_array[harrisonburg_index,0]
print("The worst day for new reported cases in Harrisonburg city is " + worst_harrisonburg_cases_date)

rockingham_seven_day_list = list()
for i in range(6,len(rockingham_data_array)):
    seven_day_cumulative_r = rockingham_data_array[i,4] + rockingham_data_array[i-1,4] + rockingham_data_array[i-2,4] + rockingham_data_array[i-3,4] + rockingham_data_array[i-4,4] + rockingham_data_array[i-5,4] + rockingham_data_array[i-6,4]
    rockingham_seven_day_list.append(seven_day_cumulative_r)

seven_day_index_r = argmax(rockingham_seven_day_list)
seven_day_date_1_r = rockingham_data_array[seven_day_index_r - 6,0]
seven_day_date_2_r = rockingham_data_array[seven_day_index_r,0]
print("The worst seven day period in Rockingham county was from " + seven_day_date_1_r + " to " + seven_day_date_2_r)

harrisonburg_seven_day_list = list()
for i in range(6,len(harrisonburg_data_array)):
    seven_day_cumulative_h = harrisonburg_data_array[i,4] + harrisonburg_data_array[i-1,4] + harrisonburg_data_array[i-2,4] + harrisonburg_data_array[i-3,4] + harrisonburg_data_array[i-4,4] + harrisonburg_data_array[i-5,4] + harrisonburg_data_array[i-6,4]
    harrisonburg_seven_day_list.append(seven_day_cumulative_h)

seven_day_index_h = argmax(harrisonburg_seven_day_list)
seven_day_date_1_h = harrisonburg_data_array[seven_day_index_h - 6,0]
seven_day_date_2_h = harrisonburg_data_array[seven_day_index_h,0]
print("The worst seven day period in Harrisonburg city was from " + seven_day_date_1_h + " to " + seven_day_date_2_h)


