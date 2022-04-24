#d. Write a Python program to convert a tuple to a string.
#Khushi Ranpariya 20CE118
tpl = ('one','two','three')

str='' #empty str into which the tupple will be converted
for i in tpl:
    str=str+i #conversion of each element to string and adding them together to convert tupple to string

print(str)
