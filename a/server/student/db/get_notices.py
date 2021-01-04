from server import *
from pymongo import *

cluster = MongoClient('mongodb+srv://Ranuga:Ranuga2008@cluster0.ahcdj.mongodb.net/<dbname>?retryWrites=true&w=majority')
student_db = cluster["NOTICES"]
student_collection = student_db["NOTICES"]


def get_notices():
    notices = []
    for notice in student_collection.find():
        notices.append(notice)
    for x in notices:
        print(x)
    print(notices)
    return notices
