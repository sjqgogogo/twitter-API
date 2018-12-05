import pymongo



def mango_search_label(key):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mongo_mini3"]
    dblist = myclient.list_database_names()
    mycol = mydb["twitter"]
    a = []
    myquery = {'label':'games'}
    for x in mycol.find(myquery):
    	a.append(x)
    return a

'''for test

for x in mango_search_label('games'):
	print('调用：',x)
'''


