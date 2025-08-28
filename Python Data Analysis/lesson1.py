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

print("          ")
print("                   ")

## below is practice of Dictionaries 

passengers_info={
    "Name": "Gemachis Tesfaye",
    "Age" : 21,
    "Seat": "12A",
    "From": "Addis Ababa",
    "To": "Hawassa",
}
print(passengers_info)
print(type(passengers_info))
print(len(passengers_info))
print(passengers_info["Name"])
print(passengers_info["Age"])
print(passengers_info["Seat"])
print(passengers_info["From"])
print(passengers_info["To"])

passengers_info["Age"]=22  ## update the age
passengers_info["Seat"]="14B"  ## update the seat
print(passengers_info)

passengers_info["Country"]="Ethiopian"  # added new key and their value
print(passengers_info)

del passengers_info["From"]  # removed From key from dictionary
print(passengers_info)

# next is list+dictionary  which is list of dictionary

print("          ")
print("                   ")

Passenger= [
    {"name": "Gemachis Tesfaye", "Age":21, "Seat":"12A", "Destination":"Adama"},
    {"name":"Sisaay Tasew", "Age": 22, "Seat":"17B", "Destination":"Bishoftu"},
    {"name":"Bonsa Tilahun", "Age":23, "Seat":"10C", "Destination": "Mojo"},
    {"name":"Samuel Tilahun", "Age": 21, "Seat":"9B", "Destination":"Addis"},
    {}
]




