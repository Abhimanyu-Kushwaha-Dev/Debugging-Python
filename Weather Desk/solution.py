import weatherdesk
city_name=input()
base_price=float(input())
order_last_hour=int(input())
riders_online=int(input())


pressure=order_last_hour/riders_online
surge=0
reason="No Reason"
temp, rain = weatherdesk.weather_now(city_name)
if rain>0 and pressure>3:
    surge=1.5
elif rain>0:
    surge=1.3
elif temp>=33 and pressure>3:
    surge=1.4
elif temp>=33:
    surge=1.2
elif pressure>4:
    surge=1.25
else:
    surge=1.0

price=base_price*surge

print("Temperature: ",temp,"C")
print("Rain: ",rain,"mm")
print("Orders per rider:",pressure)
print("Surge: ",surge)
print("Price:",price)
