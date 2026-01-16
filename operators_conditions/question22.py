def eligible_discount_or_membership(purchase, has_loyalty_card):
    return purchase > 200 or has_loyalty_card

purchase = float(input("Enter purchase amount: "))
loyalty_card = input("Do you have a loyalty card? (yes/no): ").lower() == 'yes'
result = eligible_discount_or_membership(purchase, loyalty_card)
print(f"Purchase Amount: {purchase}")
print(f"Loyalty Card: {loyalty_card}")
print(f"Eligible for discount or membership: {result}")