def calculate_discount(purchase_amount):
    if purchase_amount >= 5000:
        discount_rate = 0.20
    elif purchase_amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = purchase_amount * discount_rate
    final_payable_amount = purchase_amount - discount_amount
    return discount_amount, final_payable_amount


purchase_amount = float(input("Enter purchase amount in ₹: "))
discount, payable = calculate_discount(purchase_amount)

print(f"Discount amount: ₹{discount:.2f}")
print(f"Final payable amount: ₹{payable:.2f}")