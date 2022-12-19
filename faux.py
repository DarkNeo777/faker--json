import matplotlib as plt
import numpy as np
from faker import Faker
from faker.providers import color
from faker.providers.misc import BaseProvider
import json

fake = Faker()
#fake.add_provider(color)
fake.add_provider(json)

people = []

for i in range(5):
    people.append(fake.json(indent = 3,data_columns={'Name':'name','Color':'color_name','Address':['address']}, num_rows=1))
    #print(y)

x = json.dumps(people, indent=5)
with open("sample.json",'w') as outfile:
    outfile.write(x)