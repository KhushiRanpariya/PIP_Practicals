#e. Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#Khushi Ranpariya 20CE118
dict1={1:'one', 2:'two'}
dict2={3:'three', 4:'four'}
dict3={5:'five', 6:'six'}
#** helps to concatenate multiple dictionaries in a new dict 
dict4={**dict1,**dict2,**dict3}
print(dict4)

