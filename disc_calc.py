total = float(raw_input("Total in shopping cart:"))
discount_type = raw_input("Percentage type: percentage or dollar amount?")
discount = float(raw_input("Discount:"))
		
if discount_type == 'percentage':
	discount_amount = total*discount
		
if discount_type == 'dollar':
	discount_amount = discount
		
print discount_amount