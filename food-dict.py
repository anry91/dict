order = {
    'client': 'Jhon Doe', 
    'item'  : 'Salad', 
    'quantity': 8, 
    'price': 15.00


}
order['total'] = order['price'] * order['quantity']
#hw  6:50
if order['quantity']>7:
    order['total'] = (order['price'] * order['quantity'])-(order['price'] * order['quantity'] *0.2)

else:
    order['total'] = order['price'] * order['quantity']
choose = input('Do you need delivery? Yes/No: ')
if choose == "Yes" and order['total']>300:
    order['delivery']='free'
if choose == 'Yes' and order['total']<300:
    order['delivery']= 50.00
    order['total'] = order['total'] + order['delivery']

else:
    exit
print(order)