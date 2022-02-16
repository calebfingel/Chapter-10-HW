import InsectClass as c

mosquito = c.Insect()
housefly = c.Insect()


mosquito.flight()
housefly.flight()

print("the mosquito can fly up to", mosquito.get_flight_length(),"miles")      
print("the housefly can fly up to", housefly.get_flight_length(),"miles")
           


