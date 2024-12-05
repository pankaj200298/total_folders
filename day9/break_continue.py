
capitals = {
             "PAKISTAN": "islamabad",
             "PERU" : "LIMA",
             "GHANA": "ACCRA",
             "INDIA" : "mumbai",
             "PHILLIPINS" : "manila"
 }

user_input = "india"

for country , capital in capitals.items() :
    print(f"current contry is : {country}")
    if user_input.lower() == country.lower() :
        print(f" capital is  : {capital}")
        break
    else:
        continue
        


