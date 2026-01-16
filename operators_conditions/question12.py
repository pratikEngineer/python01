def eligible_discount_or_shipping(purchase):
    return purchase > 150 or purchase > 100

purchase = float(input("Enter purchase amount: "))
result = eligible_discount_or_shipping(purchase)
print(f"Purchase Amount: {purchase}")
print(f"Eligible for discount or free shipping: {result}")