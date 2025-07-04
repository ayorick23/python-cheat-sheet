#Probleema de la moneda (cambio minimo)
def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while coin <= amount:
            amount -= coin
            count += 1
    return count if amount == 0 else -1