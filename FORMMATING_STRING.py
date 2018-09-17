# built-in Python function orethod called forMat
# Another Bilt-in Function called Eval
name="michel";grade="A+"
"The student's name is {} and the grade is {}".format(name,grade)
#print("The student's name is {} and the grade is {}".format(name,grade))

animals=["Lions","zebras","elephants"]
safari="I saw lions,zebras and elephants!"

safari.format(animals[0],animals[1],animals[2])
#print(safari.format(animals[0],animals[1],animals[2]))

num="200"
eval(num)+10
#print(eval(num)+10)

numbers=[10,20,30,40]
eval("{}+{}+{}+{}".format(*numbers))
#print(eval("{}+{}+{}+{}".format(*numbers)))


"%d * %d = %d" % (5,3,(5*3))
#print("%d * %d = %d" % (5,3,(5 * 3)))

"%d * %d = %f" % (5,3,(5/3))
#print("%d * %d = %f" % (5,3,(5/3)))

"%d * %d =%.1f" % (5,3,(5 / 3))
#print("%d * %d =%.1f" %(5,3,(5 / 3)))

"%d * %d =%.2f" % (5,3,(5 / 3))
#print("%d * %d =%.2f" %(5,3,(5 / 3)))

"%d * %d =%.3f" % (5,3,(5 / 3))
#print("%d * %d =%.3f" %(5,3,(5 / 3)))

word="awesome"
"The lengthof this word {} is {}".format(word,len(word))
#print("The lengthof this word {} is {}".format(word,len(word)))

"days left are {num: .10f}".format(num=300/9)
#print("days left are {num: .1f}".format(num=300/9))

"days left are {num: .10f}".format(num=300/9)
#print("days left are {num: .10f}".format(num=300/9))

num=300/9
f"days left are {num:.10f}"
#print(f"days left are {num:.10f}")

p1="Python";p2="older"

F"""This is a doc string that uses {p1} 3.6 and can,t be used for {p2} varsions of {p1}""".replace("\n","").upper()
print(F"""This is a doc string that uses {p1} 3.6 and can,t be used for {p2} varsions of {p1}""".replace("\n","").upper())
print(F"""this is a doc string that uses {p1} 3.6 and can,t be used for {p2} varsions of {p1}""".replace("\n","").capitalize())


