list_task = ['book','chair','table','cup','ladder','cables','computer','game','phone','biscuit']
print(list_task)
new_item = list_task[4]

list_task.insert(0,new_item)
list_task.sort(reverse=True)
print(list_task)
print(len(list_task))