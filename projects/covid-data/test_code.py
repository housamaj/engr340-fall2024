import sys
import pandas
import pandas as pd

data = pd.read_csv('us-counties.csv')

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return
    """
    rockingham_data = data[data['fips'] == 51165.0]
    first_rockingham_case = rockingham_data.iloc[0, 0] # modify to include first positive covid case

    harrisonburg_data = data[data['county'] == 'Harrisonburg city']
    first_harrisonburg_case = harrisonburg_data.iloc[0,0]


    return first_rockingham_case + first_harrisonburg_case

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here
    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    return

print("The first positive cases in Rockingham County and Harrisonburg city are " + first_question(data))