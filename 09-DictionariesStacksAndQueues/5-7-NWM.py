hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
i=0
while i < len(hotels_in_Krakow):
    print(hotels_in_Krakow[i]["name"],end = ",")
    i+=1

for i in hotels_in_Krakow:
    avr=sum(hotels_in_Krakow[i]["price"])
