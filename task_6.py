def customer_num_model(month_n):
    return 1000*(4**month_n)

customer_num_by_months = {}
for t in range(4):
    customer_num_by_months.update({t: customer_num_model(t)})

print('Function check for customer number:', customer_num_by_months)