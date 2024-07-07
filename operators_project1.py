amount_before_purchase = 1000

phone_price = 200
food_price = 300
transport_cost = 100

#addition
total_cost = phone_price + food_price + transport_cost

print(total_cost)

#substract

remaining_amount = amount_before_purchase - total_cost

print(remaining_amount)

#10% discount
cost_after_discount = total_cost * .90
remaining_amount_after_discount = amount_before_purchase - cost_after_discount

print(cost_after_discount, remaining_amount_after_discount)


