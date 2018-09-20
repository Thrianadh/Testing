####################
 ##### list #####
####################

# A list contains a sequence of values in square brackets,[].
# Each value can be float,int, string or variable
# Each value in a list is called element
# list can contain :
	# Nested list
	# Tuples
	# Dictionaries
	# And much more

###### MUTABLE ######
# Elements in a list and Dictionaries are mutable
# Elements in a tuple or string aren't mutable

######## RANGE  ########
# range generates a specified list of numbers
# Used with loops

range(10)
print(range(10))

list(range(10))
#print(list(range(10)))
list(range(0,10,2))
#print(list(range(0,10,2)))
list(range(0,10,3))
#print(list(range(0,10,3)))
list(range(-50,60,3))
#print(list(range(-50,60,3)))


nest=[[1,2,3],[4,5,6]]
#print(nest)
new=[list(range(5)),list(range(5,10))]
new
#print(new)
nest+new
#print(nest+new)

#######################################
############ Append ################
#######################################
num=[34,2,45,22]
num
#print(num)
type(num)
#print(type(num))
num.append(100)
#print(num)
#######################################

num.clear()
num
#print(num.clear())

type(num)
#print(type(num))
type([])
#print(type([]))
num.append([34,2,45,22,100])
num
#print(num)

##############################
   ####### index ##########
##############################

num
#print(num)
num = num[0]
num
#print(num[0])

###### sort ######
num.sort()
#print(num)
####################

###### reverse ######
num.reverse()
num
#print(num)
########################

########## insert ########
num.sort()
num.insert(2,200)
num
#print(num)
########## pop ########
num.sort()
#print(num)

num.pop()

#print(num.pop())
#print(num)
#######################
items=["car","robot","ball"]
items
#print(items)
items[0] = "ps4"
items
############ insert ############
items.append(num)
items
#print(items)
items[3].insert(3,["hey!"])
items
#print(items)
type(items[3][3][0])
#print(type(items[3][3][0]))



