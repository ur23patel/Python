a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
i={}
val=0
for d in a:
    if d['item'] not in i:
        i[d['item']] = d['amount']
    else:
        i[d['item']] += d['amount'] 
print(i) 
