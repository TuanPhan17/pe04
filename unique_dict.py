# w/ sample data 
# Create an empty set called to store values that aren’t repeated
# A set is used because it automatically removes duplicates
# Loop thru each dict inside sample data
# for each dict loop thru its values 
# add each value to the empty dict we created 
# if value already exist dont add it again 

data = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
    {"VIII": "S007"}
]

unique_values = set() # empty set to store unqie values 

# Loop through each dictionary in the list
for dic in data:
    for value in dic.values():  # Loop through values of each dictionary
        unique_values.add(value)  # Add value to set

print(unique_values)