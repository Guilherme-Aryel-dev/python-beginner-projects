# Snack Bar Cashier
# Reads the customer's name and the price of each item,
# then prints a receipt with the total.

name = input('Can you tell me your name? ')
burger = int(input('Burger price: '))
fries = int(input('Fries price: '))
soda = int(input('Soda price: '))

total = burger + fries + soda

print(f'Customer: {name}')
print(f'Burger: {burger}')
print(f'Fries: {fries}')
print(f'Soda: {soda}')
print(f'Total: {total}')
print(f'Thank you, {name}! Come back soon!')