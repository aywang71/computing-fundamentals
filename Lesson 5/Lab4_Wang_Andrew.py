item_prices = [10, 40, 1, 16, 25, 34, 49, 40]
for i in range(len(item_prices)):
    for x in range(i+1, len(item_prices)):
        if item_prices[i] + item_prices[x] == 50:
            print(item_prices[i], ', ', item_prices[x])
