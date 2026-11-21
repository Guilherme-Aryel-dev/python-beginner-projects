# Gym Registration System
# Collects the member's data and validates each field.

name = input('Enter your name: ')
print(f'Name: {name} | Only letters? {name.isalpha()}')

username = input('Enter your username: ')
print(f'Username: {username} | Letters and digits only? {username.isalnum()} | Lowercase? {username.islower()}')

plan = input('Enter your plan: ')
print(f'Plan: {plan} | Uppercase? {plan.isupper()}')

age = input('Enter your age: ')
print(f'Age: {age} | Only digits? {age.isnumeric()}')
age = int(age)
next_age = age + 1
print(f'Next year: {next_age}')

weight = float(input('Enter your weight: '))
print(f'Current weight: {weight} kg')
print(f'Weight type: {type(weight)}')

goal = float(input('Enter your goal: '))
target_weight = weight + goal
print(f'Goal: +{goal} kg | Target weight: {target_weight} kg')
