##############################
 ########## TUPLES ##########
##############################
# Similar to a list in that contains acollection of elements in ()
# Elements in a tuple are immutable
# Only has two functions: index and count.
######### Built in functions #########
### max
### min
### sum
### sorted

tup1=40,50,60,70,80
tup1
#print(tup1)
type(tup1)
#print(type(tup1))

Mylist=[10,20,30]
type(Mylist)
#print(type(Mylist))
tup2=tuple(Mylist)
tup2
#print(tuple(Mylist))

tup3=tup1+tup2
tup3	
#print(tup3)

tup4="cat","cat","cat","cat","dog","dog",10,10,10,10,True
tup4.count("cat")
#print(tup4.count("cat"))

tup3.index(70)
#print(tup3.index(70))

sum(tup1*2)
#print(sum(tup1*2))
sum(tup3)
#print(sum(tup3))
max(tup3)
#print(max(tup3))
min(tup3)
#print(min(tup3))

tup3
#print(tup3)

tuple(sorted(tup3))
#print(tuple(sorted(tup3)))

tup3
tuple(sorted(tup3))

