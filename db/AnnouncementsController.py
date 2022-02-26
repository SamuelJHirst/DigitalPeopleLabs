from platformdirs import user_runtime_dir
from db.connection import db

from time import time

class AnnouncementsController:
    @staticmethod
    def create_announcement(title, text, user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        db.announcements.insert_one({ 
            "title": title,
            "text": text,
            "timestamp": time(),
            "author": user_id,
            "read_by": [user_id]
        })

        return True

    @staticmethod
    def count_unreads(user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        count = db.announcements.count_documents({ "read_by": { "$nin": [user_id] } })

        return count

    @staticmethod
    def get_unreads(user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        announcements = list(db.announcements.find({ "read_by": { "$nin": [user_id] } }, { "_id": 0, "read_by": 0 }))

        authors = {}

        for author in list(map(lambda x: x["author"], announcements)):
            authors[author] = db.users.find_one({ "_id": author }, { "_id": 0, "password": 0 })

        for i in range(len(announcements)):
            announcements[i]["author"] = authors[announcements[i]["author"]]

        return announcements

    @staticmethod
    def mark_as_read(user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        db.announcements.update_many({ "read_by": { "$nin": [user_id] } }, { "$push": { "read_by": user_id } })