prices = {
    "fiction" : 200,
    "horror" : 400,
    "comics" : 600   
}

book_type = input("Enter book type(fiction/horror/comics): ").lower()
quantity = int(input("enter quantity: "))
if book_type in prices:
    total_price = prices[book_type] * quantity
    print(f"Total price for {quantity} {book_type} book is: {total_price}")
else:
    print("Invalid book type")
    
