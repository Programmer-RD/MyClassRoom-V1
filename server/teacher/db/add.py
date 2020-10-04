from server import *
from server.other import *


cluster = MongoClient('mongodb+srv://Ranuga:Ranuga2008@cluster0.ahcdj.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = cluster["AUTH"]
collection = db["AUTH"]


class Add_Student:
    def __init__(self, user_name, passwrod, email):
        self.user_name = user_name
        self.passwrod = passwrod
        self.email = email

    def check_user_name_and_password(self):
        results = []
        for result in collection.find(
            {"User Name": self.user_name, "Password": self.passwrod, "Role": "Student"}
        ):
            results.append(result)
        if results == []:
            return True
        else:
            return False

    def check_email_and_password(self):
        results = []
        for result in collection.find(
            {"Email": self.email, "Password": self.passwrod, "Role": "Student"}
        ):
            results.append(result)
        if results == []:
            return True
        else:
            return False

    def get_id(self):
        ids = []
        for id_ in collection.find():
            ids.append(id_["_id"])
        if ids == []:
            ids = 0
        else:
            ids = sorted(ids)[-1] + 1
        return ids

    def add_to_db(self):
        add_s = Add_Student(
            user_name=self.user_name, passwrod=self.passwrod, email=self.email
        )
        results = [
            add_s.check_email_and_password(),
            add_s.check_user_name_and_password(),
        ]
        if False not in results:
            collection.insert_one(
                {
                    "_id": add_s.get_id(),
                    "User Name": self.user_name,
                    "Password": self.passwrod,
                    "Role": "Student",
                    "Email": self.email,
                }
            )
            return [True, "New A Account Created ! "]
        else:
            problems = []
            if results[0] is False:
                problems.append("Some Student has the same email and password.")
            if results[1] is False:
                problems.append("Some Student has the same user name and password.")
            return [False, problems]


class Add_Data_Entry:
    def __init__(self, user_name, passwrod, email):
        self.user_name = user_name
        self.passwrod = passwrod
        self.email = email

    def check_user_name_and_password(self):
        results = []
        for result in collection.find(
            {
                "User Name": self.user_name,
                "Password": self.passwrod,
                "Role": "Data Entry",
            }
        ):
            results.append(result)
        if results == []:
            return True
        else:
            return False

    def check_email_and_password(self):
        results = []
        for result in collection.find(
            {"Email": self.email, "Password": self.passwrod, "Role": "Data Entry"}
        ):
            results.append(result)
        if results == []:
            return True
        else:
            return False

    def get_id(self):
        ids = []
        for id_ in collection.find():
            ids.append(id_["_id"])
        if ids == []:
            ids = 0
        else:
            ids = sorted(ids)[-1] + 1
        return ids

    def add_to_db(self):
        add_s = Add_Data_Entry(
            user_name=self.user_name, passwrod=self.passwrod, email=self.email
        )
        results = [
            add_s.check_email_and_password(),
            add_s.check_user_name_and_password(),
        ]
        if False not in results:
            collection.insert_one(
                {
                    "_id": add_s.get_id(),
                    "User Name": self.user_name,
                    "Password": self.passwrod,
                    "Role": "Data Entry",
                    "Email": self.email,
                }
            )
            return [True, "New A Account Created ! "]
        else:
            problems = []
            if results[0] is False:
                problems.append("Some Data Enter has the same email and password.")
            if results[1] is False:
                problems.append("Some Data Enter has the same user name and password.")
            return [False, problems]