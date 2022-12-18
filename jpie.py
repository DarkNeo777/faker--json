import matplotlib.pyplot as plt 
import numpy as np
from faker import Faker
from faker.providers import address
import random
import json


############################################################# 
#number of people you want fake data for, creates fake: names, age, city
number_of_people = int(30)

############################################################# 

#creates a dictionary-> key value:pair that in json is an object
#in the dictionary creates a list called people, in json it is an array
#creates the file calls sample.json and write the dictionary to it
v = {
    "People":[]
}
json_object = json.dumps(v) #serilizes the python dictionary int json format
with open("sample.json","w") as outfile:
    outfile.write(json_object)

############################################################# 

faker = Faker()
#Faker.seed(123) #if you want to have the same data over and over

#adds a provider with is different methods with diffrent values to the faker class
faker.add_provider(address) #notice once u add provider you just have to use faker.method that the providers has

class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

#person list inizilize global
persons=[] 
for x in range(number_of_people) :
    #faker data created name, age, city
    #added to individual variable
    individual = Person(faker.name(),random.randrange(5,99),faker.city())
    #individual varaible with an instance of person appended/added to persons list
    persons.append(individual)

############################################################# 

#method that opens the sample.json and enters the fake data into it 🌎
def write_json(new_data, filename='sample.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["People"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

for y in range(number_of_people):
    #print("Name:",persons[y].name,"Age:",persons[y].age,"City:",persons[y].city)
    
    #calls thefunction write_json to enter the fake data into the json file, in the person list
    write_json(persons[y].__dict__)

################################################################

"""
💕💕💕💕💕💕💕
"""
