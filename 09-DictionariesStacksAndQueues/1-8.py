price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
total=0
for key,value in price_list.items():
    print(f'{key}:{value}')
#     total+=value
# print(total)
total_before = sum(price_list.values())
print(total_before)

for item in price_list:
    price_list[item] = round(price_list[item] * 0.90, 2)

for key,value in price_list.items():
    print(f'{key}:{value}')

total_after = sum(price_list.values())
print(total_after)