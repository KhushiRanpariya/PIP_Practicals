#c. Write a Python program to sum all the items in a dictionary.
#Khushi Ranpariya 20CE118
dict = {'a':10, 'b':15, 'c':20, 'd':25}
sum=0
#add values of all the elements using a for loop
for i in dict.values():
    sum=sum+i
print(sum)