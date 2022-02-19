from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.digipeoplelabs

import hashlib

class UserController:
    @staticmethod
    def create_user(first_name, last_name, job_title, username, password):
        hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), "secret".encode("utf-8"), 100000)
        
        existing_user = db.users.find_one({ 
            "username": username 
        })

        if existing_user is not None:
            return False
        
        db.users.insert_one({ 
            "first_name": first_name,
            "last_name": last_name,
            "job_title": job_title,
            "username": username, 
            "password": hashed_password 
        })

        return True

    @staticmethod
    def auth_user(username, password):
        hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), "secret".encode("utf-8"), 100000)
        
        existing_user = db.users.find_one({ 
            "username": username,
            "password": hashed_password
        })

        if existing_user is None:
            return False
        return True

    @staticmethod
    def get_user(username):
        user = db.users.find_one({
            "username": username
        })

        if user is None:
            return None

        del user["_id"]
        del user["password"]

        return user

    @staticmethod
    def delete_user(username):
        deletion = db.users.delete_one({
            "username": username
        })

        if deletion.deleted_count > 0:
            return True
        return False