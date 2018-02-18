# C&S FoodStop
# Samantha Ngo & Carol Pan
# SoftDev2 pd7
# K04 - Mi only nyam ital food, mon!
# 2018-02-15

from pymongo import MongoClient
import json

# step 1:
c = MongoClient('lisa.stuy.edu')
# step 2:
db = c.test
res = db.restaurants

# restuarants in a specified borough
def by_borough(b):
    results = res.find({"borough": b})
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

# restuarants in a specified zip code
def by_zip(z):
    results = res.find({"address.zipcode": z})
    lst = []
    for doc in results:
        lst.append(doc)
    return lst

'''
m = by_zip("10282")
print m
for doc in m:
    print "DOC: ", doc
    print doc["cuisine"]
    print doc["name"]
    print "\n"  
# works, not as many results
'''

# restaurants in a specified zip code and with a specified grade
def by_zip_grade(z,g):
    results = res.find({"address.zipcode":z , "grades.grade":g})
    lst = []
    for doc in results:
        lst.append(doc)
    return lst

'''test
n = by_zip_grade("10282","B")
print n
for doc in n:
    print doc
# works, one result
'''

# restaurants in a specified zip code with a score below a specified threshold
def by_zip_score(z,s):
    results = res.find({"address.zipcode":z, "grades.score": {"$lte" : s}})
    lst = []
    for doc in results:
        lst.append(doc)
    return lst

'''test
o = by_zip_score("10282",15)
print o
for doc in o:
    print doc
# works, several results
'''

#Something more clever.
def by_borough_cuisine_score(b,c,s):
    results = res.find({"borough":b, "cuisine":c, "grades.score": {"$lte" : s}})
    lst = []
    for doc in results:
        lst.append(doc)
    return lst

'''test
p = by_borough_cuisine_score("Manhattan", "Mexican", 5)
print p
for doc in p:
    print doc
# works, many results
'''

# step 3 & 4:
location = "usrep.json"

def getjson(path):
    with open(path, 'r') as f:
        j = json.loads(f.read())
        ret = j["objects"]
        #for l in ret:
        #    print l,"\n"
    return ret

col = db.csFoodStop
rep = getjson(location)
col.insert_many(rep)

def test():
    results = col.find({"state": "AL"})
    return results
