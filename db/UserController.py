from db.connection import db

import hashlib
from pymongo import ASCENDING

class UserController:
    @staticmethod
    def create_user(first_name, last_name, job_title, email_address, admin, username, password):
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
            "email_address": email_address,
            "admin": admin,
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
    def search_users(query):
        users = db.users.find({
            "$or": [
                {
                    "first_name": { "$regex": query, "$options": "i" }
                },
                {
                    "last_name": { "$regex": query, "$options": "i" }
                }
            ]
        }, {
            "password": 0,
            "_id": 0
        })

        users.sort([("first_name", ASCENDING), ("last_name", ASCENDING)])

        return list(users)

    @staticmethod
    def delete_user(username):
        deletion = db.users.delete_one({
            "username": username
        })

        if deletion.deleted_count > 0:
            return True
        return False