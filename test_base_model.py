#!/usr/bin/python3
print("\t\tHbtn: start of test")
from models.base_model import BaseModel


my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print("\t\tHbtn:my_model:")
print(my_model)
print()
my_model.save()
print("\t\tHbtn: my_model, after save")
print(my_model)
print()
my_model_json = my_model.to_json()
print("\t\tHbtn: my_model_json")
print(my_model_json)
print()
print("\t\tJSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("\t\tHbtn: end of test")
