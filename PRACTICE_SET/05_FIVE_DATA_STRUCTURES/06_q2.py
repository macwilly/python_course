def highest_price(product_dict):
    return max(product_dict, key=product_dict.get)


products = {
    "Laptop": 80000,
    "Phone": 60000,
    "Tablet": 35000,
    "Monitor": 15000
}
print(highest_price(products))