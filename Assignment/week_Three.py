# Question one
print("Hello World")

price=200
discount_percent= 25

def calculate_discount( price, discount_percent):
    
    if discount_percent>=20:
        discount_amount = price * (discount_percent/100)
        final_price = price- discount_amount
        return(final_price)
        
    else:
        return (price)
    
    # # Example
    # price= 100
    # discount= 25
    # final_price= calculate_discount(price, discount)
    # print(f"Final price after{discount}% discount:{final_price}")
    
    