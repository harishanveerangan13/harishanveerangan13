# from collections import Counter
#
# print(Counter(['B','B','A','B','C','A','B',
#                'B','A','C']))
#
# print(Counter({'A':3, 'B':5, 'C':2}))
#
# print(Counter(A=3, B=5, C=2))
#
# #Basically, they all print the same thing
# #will print all the counts of each value and will display them in a dictionary format from greatest amount of values to least
#
from collections import OrderedDict
#
# print("This is a dictionary:\n")
#
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
#
# for key, value in d.items():
#     print(key, value)
#
# #regular dictionary
#
print("\nThis is an ordered dictionary:\n")

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

#ordered dictionary

#at first, they do not have much difference but when adding items back to ordereddict, it will do this:

#when deleting an item in an ordered dictionary, and re-inserting it back, it will be automatically pushed to the back of the dict
od.pop('a')

od['a'] = 1
#
print("\nAfter popping and inserting:\n")

for key, value in od.items():
    print(key, value)

# from collections import defaultdict
#
# #defining the dict
# d = defaultdict(int) #datatype passed as an argument
#
# L = [1, 2, 3, 4, 2, 4, 1, 2]
# #list of numbers we want to add to the dict
#
# for i in L:
#     d[i] += 1
#
# print(d)
# #it will order all dictionary keys from least to greatest
#
# f16 = defaultdict(list) #listtype passed as an argument
#
# for i in range(5):
#     f16[i].append(i)
#
# print("Dictionary with values as list: ")
# print(f16) #values will be printed in a list format while the keys are normal
#
# from collections import ChainMap
#
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}
#
# #3 dictionaries we want to combine using chainmap
#
# ch = ChainMap(d1, d2, d3)
#
# print(ch)
#
# #chainmap will simply combine all the dictoinaries in a tuple format and print out them all
#
# print(ch['a'])
#
# print(ch.values())
#
# print(ch.keys())
#
# #you can also access the values of a chainmap and print them individually like the keys and values alone
# #
# import collections
#
# dic1 = {'a':1, 'b':2}
# dic2 = { 'b' : 3, 'c' : 4 }
# dic3 = { 'f' : 5 }
#
# chain = collections.ChainMap(dic1, dic2)
#
# print("All the ChainMap contents are: ")
# print(chain)
#
# chain1 = chain.new_child(dic3)
#
# print("displaying new chainmap: ")
# print(chain1)
# from collections import namedtuple
#
# #declaring the tuple with name
#
# student = namedtuple("Student",['name','age','DOB']) #notice how there are strings used to represent the value placeholders
#
# #adding the values to the namedtuple
# s = student('Nandini', '19', '2541997')
#
# #accessing the index
# print("The students age is: ")
# print(s[1]) #you can use the index value of the namedtuple to access the value
#
# print("Using the keyname of the namedtuple, the student's name is: ")
# print(s.name) #you can use the keyname of the tuple
#
# li = ['Manjeet', '19', '411997']
# di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }
#
# print ("The namedtuple instance using iterable is  : ")
# print(student._make(li))
# #using make to return a namedtuple