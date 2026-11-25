# Ride Receipt
# Reads the ride data and prints a receipt with the total and the price per passenger.
base_fare = 5.00
price_per_km = 2.10
price_per_minute = 0.35

name = input('Enter the passenger name: ')
plate = input('Enter the car plate: ')
distance = float(input('Enter the distance (km): '))
duration = int(input('Enter the duration (minutes): '))
number_of_passengers = int(input('Enter the number of passengers: '))

distance_price = price_per_km * distance
time_price = price_per_minute * duration

total = distance_price + time_price + base_fare
price_per_passenger = total / number_of_passengers

title = 'TRIP RECEIPT'

print('=' * 30)
print(f'{title:^30}')
print('=' * 30)

print(f'Passenger name: {name} | Only letters? {name.isalpha()}')
print(f'Plate: {plate} | Valid? {plate.isalnum()} | Uppercase? {plate.isupper()}')
print(f'Distance: {distance} km')
print(f'Duration: {duration // 60}h {duration % 60} min')

print('-' * 30)
print(f'Base fare:     R$ {base_fare:>10.2f}')
print(f'Distance:      R$ {distance_price:>10.2f}')
print(f'Time:          R$ {time_price:>10.2f}')
print('-' * 30)
print(f'TOTAL:         R$ {total:>10.2f}')
print(f'Per passenger: R$ {price_per_passenger:>10.2f}')
print('=' * 30)