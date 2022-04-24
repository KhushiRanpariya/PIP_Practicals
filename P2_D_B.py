#b. Write a Python script to merge two Python dictionaries.
#Khushi Ranpariya 20CE118
dict1 = {1:'blue', 2:'green', 3:'white', 4:'purple'}
dict2={5:'apple',6:'banana',7:'cherry',8:'grapes'}
#update() function will upate a dict by adding all the elements of another dict at its end
dict2.update(dict1)
print(dict2)
