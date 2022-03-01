import StudentClass as c

studid = (89569)
nam = ("Mason")
dob = ('1/1/2011') 
classif = ("Junior")

cell_phone = c.phone(man,mod,ret)


print("The phones manufacturer is", cell_phone.get_manufact())
print("The phones model is", cell_phone.get_model())
print("The phones reatil price is", cell_phone.get_retail_price())

cell_phone.set_manufact('Verizon')
cell_phone.set_model('iPhone')
cell_phone.set_retail_price(800)

print("The phones manufacturer is", cell_phone.get_manufact())
print("The phones model is", cell_phone.get_model())
print("The phones reatil price is", cell_phone.get_retail_price())