from main import collection

"""dictionary = {'name':'Ritwick', 'marks':89}
collection.insert_one(dictionary)"""

insertThese= [
    {'Name': 'Rajdeep', 'Location':'Bally','Marks':45},
    {'Name': 'Pritha', 'Location':'Bandel','Marks':98},
    {'Name': 'Pallabi', 'Location':'Icchapur','Marks':63},
    {'Name': 'Prateev', 'Location':'Mankundu','Marks':57}
]

collection.insert_many(insertThese)
