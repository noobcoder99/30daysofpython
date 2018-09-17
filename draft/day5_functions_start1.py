items = ["Mic", "Phone", 323.12, 31259.145, "Dan", "bag", "Bars", 1234]

str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass

print(str_items)
print(num_items)

def parse_lists(abc):
    str_list_items = []
    num_list_items = []
    for i in abc:
        if isinstance(i, float) or isinstance(i, int):
            num_items.append(i)
        elif isinstance(i, str):
            str_items.append(i)
        else:
            pass
    return str_list_items,num_list_items

print(parse_lists(items))    
