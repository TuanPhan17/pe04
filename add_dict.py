# two dicts each w/ key value pairs 
# make an empty dict 
# Loop thru each key in first dict
# If they key exist in 2nd dict 
# add values and store the sum in the dict we created 
# other wise if it only exixst in first dict store it 
# Loop thru 2nd dict 
# For each key that is not already in dict we created add it 
# Print outcome 

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

outcome = {} # Empty dict to combine results 

for key in d1: # Loop thru each key in 1st dict
    if key in d2: # If the key also exist in 2nd dict
        outcome[key] = d1[key] + d2[key] # Add values from both dicts and store sum
    else:
        outcome[key] = d1[key] #If key only exist in 1st dict , keep the value 

for key in d2: # Loop thru each key in 2nd dict
    if key not in outcome: # If they key isn't in outcome
        outcome[key] = d2[key] # Add that key to the outcome dict

print(outcome)

