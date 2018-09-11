        ###############
        # Basic Rules #
        ###############

#  Blocks can contain statements and expressions
#  Expressions can be combined to create more complex expressions
#  Most statements contain one or more expressions and nested blocks

 ######## ######### #########
######## Expressions #########
 ######## ######### #########

# Represent the idea of using input data to determine output data
# 5 is a very Simple Expression; the input number 5,and then we do nothing to it,so the output is also the number 5
# 7+3 is also an expression,which combines two other expressions to figure out an output value of 10, and (7+3)-8 ia an Expression too

 ########  ######## ########
######## Statements  ########
 ########  #######  ########

# must be place directly inside a block
# Do not'snap together' the wat expression do
# Express ideas like 'execute these instructions multiple times' or 'decide ehether to execute these unstructions'

 ########  ###### ########
########  Blocks   ########
 ######## ####### ########

# Every pthon  source code file is a block
# Many statements contain nested blocks
# Nested blocks start with a colon(:) at the end of a line, and then the lines of the block are intended

print(2+2)
print(2**16)
print(19-9)
#help()

# Variables and Data types
# Utility of variables
# Relationship between datatypes and variables
# variable is a name given to a piece of information

######### ######### ######### ######### #########
####### Reasons for using Variables    #########
######### ######### ######### ######### #########

# Makes code Easier
# Stores final value of the expression
# Easy to follow
# the value of variable can change
greet="Hello"
print(greet)
# This is a variable assignment statement. The word great is the name  of the variable, and the word "Hello" is the value.
greet+'World'
print(greet+ ' World')
# This is an expression that uses the value of the variable called greet.
 ######## ######## ########
###### Variables Names ######
 ######## ######## ########

 # Must start with a letter or an underscore,such as:
 	# _underscore
 	# underscore_
 # May consist of letters,numbers ,and underscores such as:
    # password1
    # nOOb
    # Un_der_scores
 # should be descriptive and easy to read:
 	#camelCase
 	# snake_case
 	# ALL_caps
 		# Streamofconsciousnesscase
 		# single letter names should not store impoertant values or be used on more than a couple of lines
# starting with 2_symbol is a python convention that means "don't mess with this"

# ways to input informations in variables 
	# Accepting speech input in HTML5 forms
	# Console input


###### ###### ###### ###### 
   ### Console Input ###
###### ###### ###### ###### 

# Expressions in python are:
	# input information from user
	# Retrieving the information

# Reading from and Writing to the console

from operator import add
add(3,5)
print(add(3,5))

input("Type your name: ")
name=input("Type your name: ")
print(name)
print("Your name is ",name)

# Working with Strings

###### ##### ##### ##### ##### #####
 ##### nature of Strings      #####
 ##### Ways to create strings #####
 ##### Perform operations     #####
###### ##### ##### ##### ##### #####


