from server import *
from pymongo import *

cluster = MongoClient('mongodb+srv://Ranuga:Ranuga2008@cluster0.ahcdj.mongodb.net/<dbname>?retryWrites=true&w=majority')
student_db = cluster["NOTICES"]
student_collection = student_db["NOTICES"]
def add_notice(title, description):
    student_collection.insert_one({"Title": title, "Description": description})
