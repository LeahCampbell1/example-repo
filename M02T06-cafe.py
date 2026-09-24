# Creates list "cafe items"
menu = ["coffee", "tea", "cupcakes", "biscuit", "shortcake", "sandwich", "panini"]

# Creates dictionary of menu item stock 
stock = {
        "coffee":30,
        "tea":70,
        "cupcakes":4,
        "biscuit":9,
        "shortcake":2,
        "sandwich":8,
        "panini":4
    }

# Creates dictionary of menu item prices
price = {
        "coffee":12,
        "tea":14,
        "cupcakes":3.8,
        "biscuit":1.8,
        "shortcake":2,
        "sandwich":6,
        "panini":4
    }

# Set counter for menu item iteration at 0
i = 0

# Set value for total stock at zero
total_stock = 0


# While loop iterates through menu items
while i < len(menu):
    # Key for menu item is returned from looping index
    # and used to extract value from dictionaries
    total_stock += (stock[menu[i]] * price[menu[i]])
    # Counter is increased     
    i += 1

print(f"The total value of the stock is £{total_stock}")