price = {
    "Books":20,
    "Copy":50,
    "Pen":10
}

quantity = {
    "Books":220,
    "Copy":509,
    "Pen":1150
}

money_spent = 0
for i in price:
    money_spent = money_spent + (price[i]*quantity[i])

print(money_spent)