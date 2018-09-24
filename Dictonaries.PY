# CONSISTS OF KEYS AND KEY VALUES SEPARATED BY A COLON
# Dictionaries, called dict, can contain:
	# Strings and numbers
	# tuples
	# lists
	# Sereies
	# dataframes
	# nested dictionaries

d1={}	
type(d1)
#print(type(d1))
d1["A"]=10
d1["B"]=20
d1["c"]=50
d1
#print(d1)

toys={"robot":40,"car":50}
toys
#print(toys)
toys.update(d1)
toys
#print(toys)

toys.values()
#print(toys.values())

list(toys.values())
print(list(toys.values()))

list(toys.values())[0]
#print(list(toys.values())[0])

tuple(toys.values())[0]
#print(tuple(toys.values())[0])	

toys.keys()
print(toys.keys())


maze={"k1":list(range(4)),
	  "k2":tuple(range(4,8)),
	  "k3":(1,2,3,{"K4":[1,2,3,"found you",4,5,]})}
maze
#print(maze)

maze["k3"]
#print(maze["k3"])

maze["k3"][3]
#print(maze["k3"][3])

maze["k3"][3]["K4"]
#print(maze["k3"][3]["K4"])

maze["k3"][3]["K4"][3]
#print(maze["k3"][3]["K4"][3])

