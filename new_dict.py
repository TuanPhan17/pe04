#create a dict called new dict 
#Update it with update().
#Print new dict 

#Dictionaries from lab
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

new_dict = {} #created an empty dict, to place other dicts in 

#update method to place dict's in new_dict
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict) #print the new dict 


