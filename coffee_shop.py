menu ={
    "coffee": 15,
    "tea": 10,
    "cappuccion": 55
}
order = "tea"
quantity = 3
if order.lower() in menu:
    total = menu[order.lower()] * quantity
    print(f"Total price for {quantity} {order} is: {total}")
else:
    print("Invalid order")
    
    