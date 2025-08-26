purchase_price=int(input("enter the purchase price"))

profit_margin=int(input("enter the profit margin in %"))

GST=8

profit=(profit_margin/100)*purchase_price

selling_price = purchase_price+profit

gst_amount=(GST/100)*selling_price

total_cost= selling_price+gst_amount

print(total_cost)