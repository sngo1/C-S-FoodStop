# csFoodStop
# Carol Pan & Samantha Ngo
# SoftDev2 pd7
# K05 -- Import/Export Bank
# 2018-02-20

# Dataset Used: GovTrack's Current U.S. Representatives
# This dataset stores information on all current U.S. representatives, including
# the representative's affiliations, district, websites, social media,
# birthday, and start and end term dates.

# We imported our data by saving the data as a json file from its website
# <https://www.govtrack.us/api/v2/role?current=true&role_type=representative&limit=438>
# and then reading the objects(each representative's information is
# stored in one object) into a list. Then, we imported each object as a doc
# into a collection in the database.

from pymongo import MongoClient
import json

# Step 1:
c = MongoClient('lisa.stuy.edu')

# Step 2:
db = c.test

# Step 3 & 4:
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
    return "New collection created. Data added to collection.\n"

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
print "Total # of Reps: ", len(test)
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
test = all_current_reps()
print "Representatives currently in office: \n"
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
print "Total # of Reps: ", len(test)
'''

def by_state_initials(state):
    state = state.strip().upper()
    print "STATE: -", state
    results = col.find({ "state" : state })
    print "RESULTS: ", results
    representatives = []
    for doc in results:
        full_name = doc["person"]["firstname"] + " " + doc["person"]["lastname"]
        # print full_name, "\n"
        representatives.append(full_name)
    return representatives

'''
test = by_state_initials(" ny")
print "NY Reps: \n"
for rep in test:
    try:
        print rep
    except:
        # In regards to the following error:
        # UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019'
        # in position 6: character maps to <undefined>
        print "PLACEHOLDER -- Representative's name could not be encoded."
print "Total # of Reps: ", len(test)
'''

def by_state_and_party(state, party):
    state = state.strip().upper()
    print "STATE: -", state
    results = col.find({ "state" : state, "party" : party})
    print "RESULTS: ", results
    representatives = []
    for doc in results:
        full_name = doc["person"]["firstname"] + " " + doc["person"]["lastname"]
        # print full_name, "\n"
        representatives.append(full_name)
    return representatives

'''
test = by_state_and_party(" nj", "Republican")
print "NJ Republican Reps: "
for rep in test:
    try:
        print " ", rep
    except:
        # In regards to the following error:
        # UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019'
        # in position 6: character maps to <undefined>
        print "PLACEHOLDER -- Representative's name could not be encoded."
print "Total # of Reps: ", len(test)
'''

# GIVEN THE REPRESENTATIVE, FIND THEIR...
def find_state(firstname, lastname):
    results = col.find({ "person.firstname" : firstname, "person.lastname" : lastname })
    print "RESULTS: ", results
    representatives = []
    for doc in results:
        info = []
        state = doc["state"]
        info.append(state)
        district = doc["district"]
        info.append(district)
        # print state, "\n"
        # print doc
        representatives.append(info)
    return representatives

'''
test = find_state("Steve", "Chabot")
print "Possible states: "
for state in test:
    try:
        print "---State: ", state[0]
        print "   District: ", state[1]
    except:
        # In regards to the following error:
        # UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019'
        # in position 6: character maps to <undefined>
        print "PLACEHOLDER -- Information could not be encoded."
'''

def find_affiliation(firstname, lastname):
    results = col.find({ "person.firstname" : firstname, "person.lastname" : lastname })
    print "\nRESULTS: ", results
    representatives = []
    for doc in results:
        info = []
        state = doc["state"]
        info.append(state)
        # print state
        affiliation = doc["party"]
        info.append(affiliation)
        # print affiliation, "\n"
        representatives.append(info)
    return representatives

'''
test = find_affiliation("Steve", "Chabot")
print "Possible states: "
for state in test:
    try:
        print "---State: ", state[0]
        print "   Affiliation: ", state[1]
    except:
        # In regards to the following error:
        # UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019'
        # in position 6: character maps to <undefined>
        print "PLACEHOLDER -- Information could not be encoded."
'''

# *This method tests out the projection parameter of the .find() function, but
# does not seem to make any difference over the method used in the other
# functions
def find_description(firstname, lastname):
    results = col.find({ "person.firstname" : firstname, "person.lastname" : lastname }, { "description" : 1})
    print "\nRESULTS: ", results
    representatives = []
    for doc in results:
        description = doc["description"]
        representatives.append(description)
    return representatives

'''
test = find_description("Steve", "Chabot")
print "Possible states: "
for description in test:
    try:
        print "Description: ", description
    except:
        # In regards to the following error:
        # UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019'
        # in position 6: character maps to <undefined>
        print "PLACEHOLDER -- Information could not be encoded."
'''
