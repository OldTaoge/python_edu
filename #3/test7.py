#3-5
#3-4
#3-6
#3-7
name_list=['Fang','Cheng','Yu']
print("Come to eat with me," + name_list[0])
print("Come to eat with me," + name_list[1])
print("Come to eat with me," + name_list[2])

print("However," + name_list[0] + "can't come.")
name_list[0]="My Dear"
print("Come to eat with me," + name_list[0])
print("Come to eat with me," + name_list[1])
print("Come to eat with me," + name_list[2])

print("I find a big desk ,guys")
name_list.insert(0,"My Dear")
name_list.insert(1,"FangChengyu")
name_list.append("Forever")
print("Come to eat with me," + name_list[0])
print("Come to eat with me," + name_list[1])
print("Come to eat with me," + name_list[2])
print("Come to eat with me," + name_list[3])
print("Come to eat with me," + name_list[4])
print("Come to eat with me," + name_list[5])

print("I cann't find the big desk ,guys./nOnly two people can come.")
print("Goodbye," + name_list.pop(2))
print("Goodbye," + name_list.pop(2))
print("Goodbye," + name_list.pop(2))
print("Goodbye," + name_list.pop(2))
print("You can come," + name_list[0])
print("You can come," + name_list[1])
del name_list[0]
del name_list[0]
print(name_list)