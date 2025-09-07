# list
food = ['galeey','sabuul','qamadi','shurbad','saliid','qumbo','qaro','çaano']
# index
food[3] = 'malab'
#print(food)

# print the list using for loop
#for i in food:
   # print(i)

# list methods
food.index('malab')
print(food)
print('---index-----11111------------')
food.count('ali')
print(food)
print('--count------2222------------')
food.sort()
print(food)
print('----sort------33333----------')
food.remove('malab')
print(food)
print('---remove-------444444----------')
food.append('shaah')
print(food)
print('----append-------55555---------')
food.extend('shaah')
print(food)
print('---extend-------6666666----------')
food.copy()
print(food)
print('---copy------77777777-----------')
food.reverse()
print(food)
print('---reverse-------8888888----------')
food.pop(6)
print(food)
print('----pop-----99999-----------')
food.insert(2,'coffee')
print(food)
print('----insert-----10101010-----------')
#food.clear()
print()