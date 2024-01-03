sandwich_orders = ['tuna', 'turkey', 'ham', 'chicken']
finished_sandwiches =[]

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)
print("\nList of sadwiches made:")
for sandwhich in finished_sandwiches:
    print(sandwhich)


print("The deli has run out of pastrami.")

# List of sandwich orders with 'pastrami' included
sandwhich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'ham', 'pastrami', 'chicken']

# Empty list to store finished sandwhiches
finished_sandwiches = []

# Loop to remve all instances of 'pastrami' from sandwhich_orders
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

# Making and printing each sandwich after removing 'pastrami'
for order in sandwhich_orders:
    print (f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

# Displaying the list of sandwiches made
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)