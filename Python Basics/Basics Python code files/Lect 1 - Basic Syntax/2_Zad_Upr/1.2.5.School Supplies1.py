pens = float(input("Pens: "))
pens_price = 5.8
total_pens_price = float(pens * float(pens_price))
markers = float(input("Markers: "))
markers_price = 7.20
total_markers_price = float(markers * markers_price)
detergent = float(input("Detergent, l: "))
detergent_price = 1.20
total_detergent_price = float(detergent * detergent_price)
discount = float(input("Discount: ")) / 100
total = float(total_pens_price + total_markers_price + total_detergent_price)
total_w_discount = float(total - total * discount)
# print('Total price: ' + str(total))
# print('Total price with discount: ' + str(total_w_discount))
print(total_w_discount)
