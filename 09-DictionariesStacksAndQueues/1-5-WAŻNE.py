countries = [
{"name":"Poland", "population":38000000},
{"name":"Russia","population":5000000},
{"name":"Japan","population":2000000},
{"name":"Sweden","population":6000000},
{"name":"England","population":67000000}
]


print('COUNTRY  POPULATION')
for i in countries:
    print(f"{i['name']:8} {i['population']}")