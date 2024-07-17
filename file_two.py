#list and its benifits

name1 =  ["ali hamza","abdul hade","azan ali","M.adil"]
print(name1)
print(name1[0])
print(name1[1])
print(name1[-1])

name : list[any] =  ["ali hamza","abdul hade","azan ali","M.adil","zakaullah","abc"]
print(type(name))
print(f'my name is {name[-2].upper()}')

#by default slicing run from left to right

name2 : list[any] =  ["ali hamza","abdul hade","azan ali","M.adil","abc"]
print(name2[0:3])
print(name2[0:2:1])
name2[0] = "Ali Hamza"
print(name2)
# del
element = [1,2,3,4,5,6,7,8,9]
print(element)
del element[0]
print(element)
#pop function
element1 = [1,2,3,4,5,6,7,8,9]
a = element1.pop()
print(a)
b = element1.pop(3)
print(b)
#append function
abc = []
abc.append("ali hamza")
abc.append("zakaullah")
abc.append("abdul hadi")
print(abc)
#list function is used to write string
efg = list("abcdefghijklmnopqrstuvwxyz")
print(efg)
#insert function
hij = ["a","b","c","d"]
hij.insert(0,"A")
print(hij)
#count function
variable = ["a", "b", "c", "d", "e", "a", "a", "f", "d", "c", "c"]
print(variable.count("c"))
#index function
names1 :list[str] = ['Sir Zia', 'Muhammad Qasim', 'Sir Inam', 'Dr Noman',"Muhammad Qasim","ali hamza"]
print(names1.index("Sir Zia"))
# names2 = names1
# print(names2)
#sort function
names :list[str] = list("ACBDEF")
print(names)
names.sort() #in-memory = change real data sort
print(names)
#sort and reverse function together
names :list[str] = list("ACBDEF")
print(names)
names.sort(reverse=True) #in-memory = change real data sort
print(names)
