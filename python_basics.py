my_list=[]
my_list=['A',"B",'C']
print(my_list)

my_list.append('D')
my_list.append(['D','E'])
print(my_list)
my_list.extend(['E','F',"LAST"])
my_list.extend('E')
print(my_list)
my_list.insert(0,"FIRST")
print(my_list)

my_list.pop()
my_list.reverse()
my_list.reverse()
my_list.pop(1)