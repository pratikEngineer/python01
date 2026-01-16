def eligible_discount_and_shipping(purchase):
    return purchase > 150 and purchase > 100

purchase = float(input("Enter purchase amount: "))
result = eligible_discount_and_shipping(purchase)
print(f"Purchase Amount: {purchase}")
print(f"Eligible for discount and free shipping: {result}")