#4-11
pizzas = ['lxq','pll','sbf','zjz','lhj','whg']
friend_pizza=pizzas[:]
pizzas.append('lly')
friend_pizza.append('qs')
print('My favourite pizza are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizza is:")
for pizza in friend_pizza:
    print(pizza)