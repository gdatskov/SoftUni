pens = input("Pens: ")
total_pens_price = float(pens) * 5.8
markers = input("Markers: ")
total_markers_price = float(markers) * 7.2
detergent = input("Detergent, l: ")
total_detergent_price = float(detergent) * 1.2
discount = float(input("Discount: ")) / 100
total = float(total_pens_price + total_markers_price + total_detergent_price)
total_w_discount = float(total - total * discount)
print(total_w_discount)
