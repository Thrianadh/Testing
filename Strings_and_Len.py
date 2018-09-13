####################
##### Strings  #####
####################
# Letters and Numbers in a String are called Elements
# Strings are Immutable
####################
#####  LEN     #####
####################
# Built-in python function or method
# Counts the numbers of elements in a string,list,set or dictionary.
greet="Hello World"
len(greet)
#print(len(greet))
cat="Meow";dog="Woof";parrot="Hello"
print(cat,dog,parrot)
print(cat,dog,parrot, sep=",")
print(cat,dog,parrot, sep="-")
print(cat,dog,parrot, end="!!")

"THIS IS A 'QUOTE' INSIDE A STRING!"
day="GOOD DAY"
night="good night"
len(day)
print(len(day))
len(night)
day.capitalize()
day
print(day)
print(day.capitalize())
print(len(night))
print(day.lower())
print(night.upper())

# string Concatination
lang="python"
"this is a cool" + lang +"course!"
print("this is a cool " + lang +" course!")

num=20
"Lecture "+str(num)+ " is on strings"
print("Lecture "+str(num)+ " is on strings")

"20"+"50"
#type(eval)
print(type(eval("45.3")))
print(eval("45.3"))
print(eval("20")+eval("50"))
print(eval("20+50"))
print(eval("20-50"))

check="a a a a B b b b c c"
check.count("a")
check.count("B")
check.count("b")
print(check.count("a"))
print(check.count("B"))
print(check.count("b"))

messy=""""\\ PLEASE #@CLEAN UP-- #@THIS MESSY #@DOCSTRING
WHICH --CAN HAVE\\ MULTIPLE LINES\\
OF STRING--"""
messy
print(messy)
messy.replace("\\","").replace("#@","").replace("--","").replace("\n","")
messy.replace("\\","").replace("#@","").replace("--","").replace("\n","").lower()
print(messy.replace("\\",""))
print(messy.replace("\\","").replace("#@","").replace("--","").replace("\n",""))
print(messy.replace("\\","").replace("#@","").replace("--","").replace("\n","").lower())

# Immutable
pet="cat"
print(pet)

print(pet[0])
#TypeError: 'str' object does not support item assignment 
pet[0]="b"
print(pet[0]="b")
