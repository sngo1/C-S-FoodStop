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

# step 3 & 4:
data = "usrep.json"

# SETUP ---------------------------------------------------------------------
# Returns a list of all the objects in a json file(the first level in the
# dictionary).
def getjson(path):
    print "Reading json file..."
    with open(path, 'r') as f:
        j = json.loads(f.read())
        list_of_objects = j["objects"]
        #for l in list_of_objects:
        #    print l,"\n"
    print "JSON file read.\n"
    return list_of_objects

col = db.csFoodStop
rep = getjson(data)

# Adds the newly read data into a collection in the database
def insert_data():
    col.insert_many(rep)
    print "New collection created. Data added to collection.\n"

# Deletes working collection in the database
def delete_data():
    col.drop()
    return "Collection dropped."

# Deletes the database and then recreates it to prevent repeats
# *This may take more storage or time, so it may not be viable in
# real-world applications
print delete_data()
print insert_data()
    
# End of SETUP ---------------------------------------------------------------

# Get representative by...
def by_gender(gender):
    results = col.find({ "person.gender" : gender })
    print "RESULTS: ", results
    representatives = []
    for doc in results:
        full_name = doc["person"]["firstname"] + " " + doc["person"]["lastname"]
        # print full_name, "\n"
        representatives.append(full_name)
    return representatives

'''
test = by_gender("female")
print "Women in Government: \n"
for woman in test:
    try:
        print woman
    except:
        # In regards to the following error:
        # UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019'
        # in position 6: character maps to <undefined>
        print "PLACEHOLDER -- Representative's name could not be encoded."
print "Reps: ", len(test)
'''

def all_current_reps():
    results = col.find({ "current" : True })
    print "RESULTS: ", results
    representatives = []
    for doc in results:
        try: 
            full_name = doc["person"]["firstname"] + " " + doc["person"]["lastname"]
            # print full_name, "\n"
            representatives.append(full_name)
        except:
            representatives.append("PLACEHOLDER -- Representative's name could not be encoded.")
    return representatives

'''
test = out_of_office()
print "Representatives out of office: \n"
print test
test = test
for rep in test:
    try:
        print rep
    except:
        # In regards to the following error:
        # UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019'
        # in position 6: character maps to <undefined>
        print "PLACEHOLDER -- Representative's name could not be encoded."
print "Reps: ", len(test)
'''

