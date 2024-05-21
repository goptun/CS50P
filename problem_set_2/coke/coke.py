COST = 50
ACCEPTED_COINS = [25, 10, 5]

amount_due = COST

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert coin: "))

    if coin in ACCEPTED_COINS:
        amount_due -= coin
    else:
        print(f"Invalid coin. Accepted coins are: {ACCEPTED_COINS}")

change_owed = abs(amount_due)

print(f"Change Owed: {change_owed}")
