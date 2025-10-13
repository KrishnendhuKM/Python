fruit_shop = {
    "apple" : 80,
    "banana" : 50,
    "mango" : 70,
    "orange" : 45
}

fruit = "mango"
quantity = 5

total_cost = fruit_shop[fruit] * quantity
print(f"total cost for {quantity} of {fruit} is : {total_cost}")
