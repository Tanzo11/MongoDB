from main import collection

print(collection.find_one({'Name':'Sayandeep'}))
allDocs = collection.find({},{'_id': 0, 'Name':1}).sort({'Name':-1}).limit(4)
for item in allDocs:
    print(item)