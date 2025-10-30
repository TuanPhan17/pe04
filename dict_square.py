# Ask user to input a number
# create an empty dict 
# loop thru each number starting from 1 up to and inclduing n
# for each number calculate it x * x 
# add this pair to the empty dict called outcome 
# when loop ends print it

n = int(input("Enter a number: ")) #enter in a number 

outcome = {} # an empty to to store outcomes 

for x in range (1, n + 1): # Loop thru numbers from 1 to N
    outcome[x] = x * x # storing numbers in [x] by doing X*X

print(outcome) #print it 

