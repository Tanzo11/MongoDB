from main import collection

collection.update_one({'Name':'Sayandeep'},{'$set':{'Location':'Icchapur'}})
#collection.update_many({'Name':'Sayandeep'},{'$set':{'Location':'Icchapur'}})
#print(collection.update_many({'Name':'Sayandeep'},{'$set':{'Location':'Icchapur'}}).modified_count)