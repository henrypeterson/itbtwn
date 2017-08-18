#!/usr/bin/python

import math
import sys

class object:
    sub_objects = []

class concept(object):
    c = 0

class place(object):
    things_there = []

class hierarchy:
    def __init__(self, n):
        self.name = n
        self.power = ["destroy", "create"]
        self.scale = []

class thing(object):
    def __init__(self, n, d):
        self.lesser_things = []
        self.attributes = {
                "name": n,
                "description": d,
                }

list_of_objects = {}

#add_att <thing> <attribute> <description>
def add_att(user_in):
    obj = list_of_objects.get(user_in[0], False)
    if(obj != False):
        obj.attributes[user_in[1]] = user_in[2]

'''
#set_power <thing1> <"<",">"> <thing2>
def set_power(user_in):
    thing1 = list_of_objects.get(user_in[0], False)
    thing2 = list_of_objects.get(user_in[2], False)
    if(not thing1 or not thing2):
        print("invalid")
        return
    if(user_in[1] == ">"):
        thing1.lesser_things.append(thing2)
    elif(user_in[1] == "<"):
        thing2.lesser_things.append(thing1)
    else:
        print("invalid power set")
'''
#set_power <hierarchy name> <thing1> <"<",">"> <thing2>
def set_power(user_in):
   #fill with stuff 

def remove(user_in):
    if(user_in[0] == "well"):
        print("oh no")

#make_thing <name> <description>
def make_thing(user_in):
    #check_input(user_in)
    list_of_objects[user_in[0]] = thing(user_in[0], user_in[1])

#make_hierarchy <name>
def make_hierarchy(user_in):
    list_of_hiers[user_in[0]] = hierarchy(user_in[0])

def default(user_in):
    print("meaningless")

def parse_command(user_in):
    base_commands.get(user_in[0], default)(user_in[1:])

def print_field(obj, count):
    sys.stdout.write(obj.attributes['name'] + "\n")
    for i in obj.lesser_things: 
        for j in range(0, count):
            sys.stdout.write("\t")
        print_field(i, count+1)

base_commands = {
        "add": add_att,
        "remove": remove,
        "thing": make_thing,
        "hierarchy": make_hierarchy,
        "power": set_power,
        }

the_pure_object = object()
list_of_objects["nothing"] = thing("nothing", "nothing")


run = True
f = open("input.txt", 'r')
while(run == True):
    #user_in = raw_input("> ")
    user_in = f.readline()
    user_in = user_in[:-1]
    if(user_in == "q"):
        run = False
    else:
        parse_command(user_in.split())
    
print_field(list_of_objects["nothing"], 0)
        


