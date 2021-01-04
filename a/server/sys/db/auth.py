from server import *

cluster = MongoClient('mongodb+srv://Ranuga:Ranuga2008@cluster0.ahcdj.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = cluster["AUTH"]
collection = db["AUTH"]


class Sign_In:
    def __init__(self, role, user_name_or_email, passwrod):
        self.user_name_or_email = user_name_or_email
        self.passwrod = passwrod
        self.role = role

    def check_user_name_and_password(self):
        results = []
        for x in collection.find(
            {
                "User Name": self.user_name_or_email,
                "Password": self.passwrod,
                "Role": self.role,
            }
        ):
            results.append(x)
        if results == []:
            return False
        else:
            return True

    def check_email_and_password(self):
        results = []
        for x in collection.find(
            {
                "Email": self.user_name_or_email,
                "Password": self.passwrod,
                "Role": self.role,
            }
        ):
            results.append(x)
        if results == []:
            return False
        else:
            return True

    def check(self):
        si = Sign_In(
            role=self.role,
            user_name_or_email=self.user_name_or_email,
            passwrod=self.passwrod,
        )
        results = [si.check_email_and_password(), si.check_user_name_and_password()]
        if results[0] is True or results[1] is True:
            return True
        else:
            return False
class Forogot_Password:
    pass