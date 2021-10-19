shop_markup = 0.75
shop_sale_price = 299.
shop_sale_markup = 0.15
 
actual_price = shop_sale_price/(1. + shop_sale_markup)
shop_markup_price = actual_price/(1. + shop_markup)

print('Common shop markup price:', round(shop_markup_price, 2))