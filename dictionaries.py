# This is a list of my information
person1 = ["Muyani Letina", "0710923458", "47", "Nairobi"]

# This is a dictionary (key value pair)
e = {"name":"Muyani Letina","phone_number":"0710923458","age":47,"location":"Nairobi",
     "marks":{"math":32,"english":45,"kiswahili":67,"ssr":45,"sci":67},
     "date_of_birth": (24, "DEC", 1994, {"born":1994, "born_again":2005})
     }
print(type(e))
print(e["phone_number"])
print(e["age"])
print(e["location"])
print(e["marks"]["ssr"])
ba = (e["date_of_birth"][3]["born_again"])
print(ba)

