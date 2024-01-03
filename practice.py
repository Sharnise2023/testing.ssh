print("The deli has run out of pastrami.")

sandwhich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'ham', 'pastrami', 'chicken']
finished_sandwiches = []

while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

for order in sandwhich_orders:
    print (f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
