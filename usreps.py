# C&S FoodStop
# Samantha Ngo & Carol Pan
# SoftDev2 pd7
# K05
# 2018-02-20

from pymongo import MongoClient
import json

# step 1:
c = MongoClient('lisa.stuy.edu')
# step 2:
db = c.test
reps = db.reps

# restuarants in a specified borough
def by_state(state):
    results = res.find({"state": state})
    lst = []
    for doc in results:
        lst.append(doc)
    return lst

'''
l = by_borough("Manhattan")
print l
for doc in l:
    print doc
# works, returns a lot of results
# NOTE:: OBJECTID IS GIVEN LAST
'''

# step 3 & 4:
data = "usrep.json"

# Returns a list of all the objects in a json file(the first level in the
# dictionary).
# LEVEL 1
def getjson(path):
    with open(path, 'r') as f:
        j = json.loads(f.read())
        list_of_objects = j["objects"]
        #for l in list_of_objects:
        #    print l,"\n"
    return list_of_objects

col = db.csFoodStop
rep = getjson(data)

def insert_data():
    # Adding level 1 data
    print "Level 1: ", rep[0], "\n"
    col.insert_many(rep)

def test():
    results = col.find({"gender": "female"})
    return results

#tester = test()
#print tester[1]
