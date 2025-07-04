#Billing:
p_name=input("Enter the product name:")
p_qty=int(input("Enter the quantity of product you want:"))
p_price=int(input("Enter the price of one product:"))
p_tax=int(input("Enter the tax of the product:"))
print('product_name  product_quantity  product_price  product_tax ')
print(' ',p_name,'       ',p_qty,'    ',p_price,'      ',p_tax )
tot_price_wo_tax= (p_qty*p_price)
tot_price_w_tax= tot_price_wo_tax - ((p_tax/100)*tot_price_wo_tax)
print("Total amount",tot_price_w_tax)



