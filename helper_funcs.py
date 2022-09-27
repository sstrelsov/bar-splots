def get_orders(name_d):
    for name in name_d:
       items_ordered = input(f"{name}'s prices: ").split()
       name_d[name] = sum([float(i) for i in items_ordered])

def create_proportions_dict(name_d):
    # calculate bill's subtotal
    bill_subtotal = 0.00
    for sub in name_d.values():
        bill_subtotal = bill_subtotal + sub

    # create new dictionary to keep track of what proportion of the subtotal each person pays
    proportions_dict = {name : 0.00 for name in name_d.keys()}
    for name,pay in name_d.items():
        prop = pay/bill_subtotal
        proportions_dict[name] = prop
    return proportions_dict

def proportionalize(bill_item, name_d,prop_d):
    for name,pay in name_d.items():
        prop = prop_d[name]
        new_individual_total = round(bill_item * prop,2)
        name_d[name] = round(name_d[name] + new_individual_total,2)

def print_receipt(name_d):
    #calculate bill total
    bill_total = 0.00
    for pay in name_d.values():
        bill_total = bill_total + pay
    print(f"Bill total: {bill_total}")