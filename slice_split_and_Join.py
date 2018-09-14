###########################################
######### SLICE APLIT AND JOIN ############
###########################################

# index,slicing and stride #
# Both split and join string methods which perform opposing operations 
# THe slice built-in python function
# Membership operator IN and nverse boolean operator NOT

##################
#### Indexing ####
##################

greet="Hello World"
greet[0]
#print(greet[0])

###################
##### slicing #####
###################

greet[6:]
#print(greet[6:])

####################
###### stride  #####
####################

letters="abcdef"
letters[1::2]
#print(letters[1::2])

###################################################

robot="Technologically"
consoles="ps4 is cooler than xbox!"
code="ply2t3h4o5n6i7c8"
words="I saw a cow fly over the moon and into the clouds"
new_words="I saw a cow fly over the gates and into the forest"
paid="I received a total of $5000"

len(robot)
#print(len(robot))
robot[0:6]
#print(robot[0:6])
robot[0:]
#print(robot[0:])
robot[6:]
#print(robot[6:])
robot[:14]
#print(robot[:14])
robot[::-1]
#print(robot[::-1])
##############################
##############################
##############################

consoles.endswith("!")
#print(consoles.endswith("!"))
consoles[7:13]
#print(consoles[7:13])
consoles[-17]
#print(consoles[-17])
consoles[23]
#print(consoles[23])
consoles[-17:-11]
#print(consoles[-17:-11])
######################################
code
#print(code)
code.replace("1","").replace("2","")
#print(code.replace("1","").replace("2",""))
code[0:1]
#print(code[0:1])
code[0:1]+code[2:3]+code[4:5]
#print(code[0:1]+code[2:3]+code[4:5])
code[0::2].upper()
#print(code[0::2].upper())
code[1::2]
#print(code[1::2])
code[1::2][::-1]
#print(code[1::2][:: -1])
code[1::2][::-2]
#print(code[1::2][::-2])
###########################################

var=words.split()
len(var)
#print(len(var))
#print(var)
var[3:8:2]
#print(var[3:])
var[3:]
#print(var[3:8:2])
var[3:8:2]

var[3:12:2]
#print(var[3:12:2])
##########################
new_words
print(new_words)
##########################

s1=slice(3,12,2)
new_words.split()[s1]
print(new_words.split()[s1])
print(var)
#print("dog" not in var and "cow" not in new_words.split()[s1])
"dog" not in var and "cow" not in new_words.split()[s1]

"".join(var)
#print("".join(var))
" ".join(var)
#print(" ".join(var))
##################
paid.split()
#print(paid.split())
paid.split("$")
#print(paid.split("$"))

paid.split("$")[0]
#print(paid.split("$")[0])
paid.split("$")[1]
#print(paid.split("$")[1])

