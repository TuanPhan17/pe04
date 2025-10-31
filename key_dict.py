# make two dicts for x and y 
# for each key value pair in 1st dict 
# check if the key also exist in the 2nd dict 
# if it does compare their values 
# if values are the same 
# print that this key and value are present in both dicts 


# sample dicts 
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for key in x: # Loop thru each key in 1st dict 
    if key in y and x[key] == y[key]: # check if key exist in 2nd dict 
        print(f"{key}: {x[key]} is present in both x and y") # if both they key and value match . Print it