amt_due = 50

while amt_due > 0:
    print(f"Amount Due: {amt_due}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amt_due -= coin

print(f"Change Owed: {abs(amt_due)}")