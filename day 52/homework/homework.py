
my_list = []

# 7 ელემენტის დამატება
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
my_list.append(70)


my_list[2], my_list[1] = my_list[1], my_list[2]


my_list.insert(4, 100)


del my_list[5]  
del my_list[0]  


print(my_list)
