import sys
import pandas
import pandas as pd

data = pd.read_csv('us-counties.csv')

rockingham_data = data[(data['fips'] == 51165.0) & (data['cases'] > 0)]

first_rockingham_case = rockingham_data.iloc[0, 0]

print("The first positive case in Rockingham occurred on: " + str(first_rockingham_case))

harrisonburg_data = data[(data['county'] == 'Harrisonburg city') & (data['cases'] > 0)]

first_harrisonburg_case = harrisonburg_data.iloc[0, 0]

print("The first positive case in Harrisonburg city occurred on: " + str(first_harrisonburg_case))

rockingham_cases_array = rockingham_data['cases'].to_numpy()

np_array_cases = rockingham_data['cases'].to_numpy()

for i in range(1,len(np_array_cases)):
    case_value = np_array_cases[i] - np_array_cases[i-1]
    if (np_array_cases[i+1] - np_array_cases[i]) > case_value:
        case_value = np_array_cases[i+1] - np_array_cases[i]
    else:
        continue

print(case_value)
