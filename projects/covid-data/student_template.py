import sys
import pandas as pd
import numpy as np

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    data = pd.read_csv('us-counties.csv') # function will read a csv file and import it as a dataframe

    rockingham_data = data[(data['fips'] == 51165.0) & (data['cases'] > 0)] # basic pandas manipulation to extract rockingham data
    first_rockingham_case = rockingham_data.iloc[0, 0] # extract the value from the 0th column and 0th row

    harrisonburg_data = data[(data['county'] == 'Harrisonburg city') & (data['cases'] > 0)] # same logic as rockingham
    first_harrisonburg_case = harrisonburg_data.iloc[0, 0]

    return print("The first positive case in Rockingham county was " + first_rockingham_case + " and the first case in Harrisonburg city was " + first_harrisonburg_case)

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    data = pd.read_csv('us-counties.csv')
    rockingham_data = data[(data['fips'] == 51165.0) & (data['cases'] > 0)]
    harrisonburg_data = data[(data['county'] == 'Harrisonburg city') & (data['cases'] > 0)]

    rockingham_data_array = rockingham_data.to_numpy() # basic function for converting a dataframe to an array
    harrisonburg_data_array = harrisonburg_data.to_numpy() # same as above

    rockingham_list = list()  # create list to store all the new covid cases instead of cumulative
    for i in range(1, len(rockingham_data_array)):
        current_max = rockingham_data_array[i, 4] - rockingham_data_array[i - 1, 4]
        rockingham_list.append(current_max)

    rockingham_index = np.argmax(rockingham_list) # use argmax function to extract the index of the max
    worst_rockingham_cases_date = rockingham_data_array[rockingham_index, 0] # access the date from that same index value in the array

    harrisonburg_list = list() # same as above
    for i in range(1, len(harrisonburg_data_array)):
        current_max = harrisonburg_data_array[i, 4] - harrisonburg_data_array[i - 1, 4]
        harrisonburg_list.append(current_max)

    harrisonburg_index = np.argmax(harrisonburg_list)
    worst_harrisonburg_cases_date = harrisonburg_data_array[harrisonburg_index, 0]

    return print("The worst day for covid cases in Rockingham county was " + worst_rockingham_cases_date + " and the worst day for covid cases in Harrisonburg city was " + worst_harrisonburg_cases_date)

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    data = pd.read_csv('us-counties.csv')
    rockingham_data = data[(data['fips'] == 51165.0) & (data['cases'] > 0)]
    harrisonburg_data = data[(data['county'] == 'Harrisonburg city') & (data['cases'] > 0)]

    rockingham_data_array = rockingham_data.to_numpy()
    harrisonburg_data_array = harrisonburg_data.to_numpy()

    rockingham_new_cases = list() # same as second question
    for i in range(1, len(rockingham_data_array)):
        current_max = rockingham_data_array[i, 4] - rockingham_data_array[i - 1, 4]
        rockingham_new_cases.append(current_max)

    rockingham_cumulative = list() # create list to store the seven-day sum of new cases
    for i in range(6,len(rockingham_new_cases)):
        seven_day_cumulative = rockingham_new_cases[i] + rockingham_new_cases[i-1] + rockingham_new_cases[i-2] + rockingham_new_cases[i-3] + rockingham_new_cases[i-4] + rockingham_new_cases[i-5] + rockingham_new_cases[i-6]
        rockingham_cumulative.append(seven_day_cumulative)

    rockingham_index = np.argmax(rockingham_cumulative)
    rockingham_first_day = rockingham_data_array[rockingham_index,0] # access the array for the first day of the period
    rockingham_second_day = rockingham_data_array[rockingham_index + 6,0] # access the array for the last day of the period

    harrisonburg_new_cases = list() # same as before
    for i in range(1,len(harrisonburg_data_array)):
        current_max = harrisonburg_data_array[i,4] - harrisonburg_data_array[i-1,4]
        harrisonburg_new_cases.append(current_max)

    harrisonburg_cumulative = list() # same as before
    for i in range(6,len(harrisonburg_new_cases)):
        seven_day_cumulative = harrisonburg_new_cases[i] + harrisonburg_new_cases[i-1] + harrisonburg_new_cases[i-2] + harrisonburg_new_cases[i-3] + harrisonburg_new_cases[i-4] + harrisonburg_new_cases[i-5] + harrisonburg_new_cases[i-6]
        harrisonburg_cumulative.append(seven_day_cumulative)

    harrisonburg_index = np.argmax(harrisonburg_cumulative) # same as before
    harrisonburg_first_day = harrisonburg_data_array[harrisonburg_index,0]
    harrisonburg_second_day = harrisonburg_data_array[harrisonburg_index+6, 0]

    return print("The worst seven day period in Rockingham county was from " + rockingham_first_day + " to " + rockingham_second_day + " and the worst seven day period in Harrisonburg city was from " + harrisonburg_first_day + " to " + harrisonburg_second_day)

data = pd.read_csv('us-counties.csv')

print(first_question(data))
print(second_question(data))
print(third_question(data))


