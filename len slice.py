toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print(num_pizzas)

print("We sell %s different kinds of pizza" %(num_pizzas))

pizzas = list(zip(prices, toppings))

print (pizzas)

sorted_prices = pizzas.sort()


print(pizzas)

cheapest_pizza = pizzas[0]

print(cheapest_pizza)

pricest_pizza = pizzas[-1]

print(pricest_pizza)

three_cheapest = pizzas[0:3]

print(three_cheapest)

count_of_2 = prices.count(2)

print("There are %s toppings that cost $2" %(count_of_2))

count_of_cheese_and_mushrooms = toppings.count('cheese')

print(count_of_cheese_and_mushrooms)