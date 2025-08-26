car={"id":1,"name":"polo","top_speed":140,"mileage":15,"offer":5}

car["mileage"]=20

if "offer" in car:
    car["offer"]+=20
else:
    car["offer"]=20

print(car["offer"])
