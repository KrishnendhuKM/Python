laptop = {
    "dell" : 50000,
    "hp" : 60000,
    "lenovo" : 45000,
    "apple" : 100000
}
brand = "lenovo"
quantity = 3
if brand.lower() in laptop:
        bill = laptop[brand.lower()] * quantity
        print(f"Total price for {quantity} {brand} is : {bill}")
else:
        print("invalid brand")