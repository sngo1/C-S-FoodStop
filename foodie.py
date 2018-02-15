# C&S FoodStop
# Samantha Ngo & Carol Pan
# SoftDev2 pd7
# K04 - Mi only nyam ital food, mon!
# 2018-02-15

from pymongo import MongoClient

# step 1:
c = MongoClient('lisa.stuy.edu')
# step 2:
db = c.test
res = db.restaurants
# step 3 & 4:

# restuarants in a specified borough
def by_borough(b):
    results = res.find({"borough": b})
    return results

'''test
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
    return results

'''test
m = by_zip("10282")
print m
for doc in m:
    print doc
# works, not as many results
'''

# restaurants in a specified zip code and with a specified grade
def by_zip_grade(z,g):
    results = res.find({"address.zipcode":z , "grades.grade":g})
    return results

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
    return results

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
    return results

'''test
p = by_borough_cuisine_score("Manhattan", "Mexican", 5)
print p
for doc in p:
    print doc
# works, many results
'''
