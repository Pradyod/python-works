bikes=[
    ["passion-pro","hero",89000,"petrol",125],
    ["passion-plus","hero",89000,"petrol",125],
    ["activa","honda",120000,"petrol",125],
    ["xpulse","hero",139000,"petrol",150],
    ["hunter","re",200000,"petrol",350],
    ["metor","re",230000,"petrol",350],
    ["triumph-speed-400x","triumph",300000,"petrol",400],
    ["ola-s1-pro","ola",140000,"ev",120],
    ["aether-450x","aether",150000,"ev",120],
]

# all_bikes=[b[0] for b in bikes]
# print(all_bikes)

# all_price=[b[2] for b in bikes]
# print(all_price)

# fuel_variants={b[3] for b in bikes}
# print(fuel_variants)

# price_filter=[b[0] for b in bikes if b[2]>100000]
# print(price_filter)

# ev_bikes=[b[0] for b in bikes if b[3]=="ev"]
# print(ev_bikes)


def max_price(lst):
    return lst[2]

max_price_bike=max(bikes,key=max_price)
print(max_price_bike)
