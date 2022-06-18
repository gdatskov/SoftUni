packages = int(input())
total_weight = 0
total_bus_packages_weight = 0
total_truck_packages_weight = 0
total_train_packages_weight = 0
for weight_sorting in range (packages):
    package_weight = int(input())
    total_weight += package_weight
    if package_weight <= 3:
        total_bus_packages_weight += package_weight
    elif package_weight <= 11:
        total_truck_packages_weight += package_weight
    else:
        total_train_packages_weight += package_weight

average_price_per_ton = (total_bus_packages_weight*200 + total_truck_packages_weight*175
                         + total_train_packages_weight*120) / total_weight

print(f"{average_price_per_ton:.2f}")
print(f"{total_bus_packages_weight/total_weight*100:.2f}%")
print(f"{total_truck_packages_weight/total_weight*100:.2f}%")
print(f"{total_train_packages_weight/total_weight*100:.2f}%")
# •	Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# •	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# •	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# •	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).
