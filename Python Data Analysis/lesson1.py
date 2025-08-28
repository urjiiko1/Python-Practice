airlines="Ethiopian Airlines"   ##string
passengers=170                   ##integer
from_city ="Addis Ababa"          ##string
to_city="Hawassa"               ##string
price="$50.3"                   ##float
date="August 27, 2025"          ##string
time="Morning"                  ##string
departure_time="2:25 LT"        ##string
arrival_time="3:05 LT"          ##string
is_flight_on_time=True          ##boolean

print(airlines, "have", passengers, "passengers that departure from", from_city, "into", to_city, 
      "the total price for this travel is" , price, "which flight is start Morning at" , departure_time, "and arrived at" , arrival_time, "is found = " ,is_flight_on_time)

## OUTPUT IS
# Ethiopian Airlines have 170 passengers that departure from Addis Ababa into Hawassa the total price for this travel is $50.3 which flight is start Morning at 2:25 LT and arrived at 3:05 LT is found =  True

print("          ")
print("                   ")
# next is list or commonly known as collecton of items

passengers_names=["Gemachis Tesfaye", "Sisaay Tasew", "Bonsa Horsa", "Samuel Tilahun", "Daniel Alemayehu"]
print(passengers_names[0])
print(passengers_names[1])
print(passengers_names[2])
print(passengers_names[3])
print(passengers_names[4])
print(passengers_names)
print(type(passengers_names))
print(len(passengers_names))
passengers_names.append("Abebe Guta")
print(passengers_names)
passengers_names.remove("Gemachis Tesfaye")
print(passengers_names)





