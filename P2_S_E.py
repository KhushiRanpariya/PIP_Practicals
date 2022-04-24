#e. Write a Python program to find the length of a tuple.
#Khushi Ranpariya 20CE118
lst=['dog','dog','dog','cat','tiger','lion']
tp=(2,2,3,4,4,4,5,6)
dct = {'a':100, 'b':100, 'c':200, 'd':250}
print(max(set(lst),key=lst.count))
print(max(set(tp),key=tp.count))
max(dct.iterkeys(), key = dct.get)