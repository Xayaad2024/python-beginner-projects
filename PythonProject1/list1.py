food = ["canjeelo","maraq","biskut","laxoox","suqaar'"]
#print(food)
food[1] = 'saliid'
# print(food[0])
# print(food[1])
# print(food[2])
# print(food[3])

food.append("bariis")
food.sort()
food.remove("bariis")
food.insert(4,"cake")
food.clear()
for i in food:
    print(i)

