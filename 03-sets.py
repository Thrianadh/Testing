# sets are built-in python class
# Based on a branch mathematics called set theory
# Outputs only the unique elements, i.e numbers,strings,booleans,etc.
s1={2,2,2,2,2,2,2,10,20,30}
s1
print(s1)

type(s1)
print(type(s1))

s2=[3,3,3,3,3,10,40,20]
s2=set(s2)
s2
print(s2)

s1.union(s2)

print(s1.union(s2))

s1.intersection(s2)
print(s1.intersection(s2))

s1.difference (s2)
s2.difference (s1)
print(s1.difference (s2))
print(s2.difference (s1))

s3={200,False,"cat"}
s1.update(s3)
print(s1)

s1.add(400)
print(s1)

s4={400,False,2}
print(s4)

s1.issuperset(s4)
print(s1.issuperset(s4))
s4.issuperset(s1)
print(s4.issuperset(s1))

tup=(10,20,30,500,500,500,"dog","True",1,1,False,0,0)
print(tup)
set(tup)
print(set(tup))

False==0
True==1
print(False==0)
print(True==1)


