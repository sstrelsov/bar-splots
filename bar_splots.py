from helper_funcs import *

names = input("Enter names: ").split()
name_dict = {name : 0.00 for name in names}

get_orders(name_dict)
proportions_dict = create_proportions_dict(name_dict)

group_charges = input("Enter top-level charges of the bill (ie tax, tip, service charge): ").split()
for i in range(len(group_charges)):
    charge = group_charges[i]
    bill_item = float(input(f"Enter bill {charge}: "))
    proportionalize(bill_item,name_dict,proportions_dict)

print(name_dict)
print_receipt(name_dict)