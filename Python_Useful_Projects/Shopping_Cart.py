# shopping cart

foods = []
prices = []

total_price = 0

while True:
    choice = input("Enter the food to buy (q to quit): ")
    if choice.lower() == "q":
        break

    else:
        price = float(input(f"Enter the price of a {choice}: $"))
        foods.append(choice)
        prices.append(price)

i=0
print("----- YOUR CART ------")
for every_food in foods:
    print(every_food, prices[i])
    i = i + 1

for every_price in prices:
    total_price += every_price

print(f"Your Total Price: {total_price}")