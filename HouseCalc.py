price_of_house=100000
is_buyer_has_credit=True
down_payment=0
if is_buyer_has_credit:
    down_payment= price_of_house * (10/100)
else:
    down_payment= price_of_house * (20/100)
print(f"Down payment required is {down_payment}")