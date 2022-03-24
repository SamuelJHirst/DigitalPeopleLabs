from db.connection import db

from pymongo import DESCENDING
from time import time

class HoursController:
    @staticmethod
    def start_shift(user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        if HoursController.has_open_shift(user):
            return False

        db.shifts.insert_one({ 
            'user': user_id,
            'startTime': time(),
            'endTime': None
        })

        return True

    @staticmethod
    def end_shift(user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        update = db.shifts.find_one_and_update({
            'user': user_id,
            'endTime': None
        }, {
            '$set': {
                'endTime': time()
            }
        })

        if not update:
            return False

        return True

    @staticmethod
    def has_open_shift(user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        update = db.shifts.find_one({
            'user': user_id,
            'endTime': None
        })

        if not update:
            return False

        return True

    @staticmethod
    def get_users_shifts(user):
        user_id = dict(db.users.find_one({ "username": user }, { "_id": 1 }))["_id"]

        shifts = db.shifts.find({
            'user': user_id
        })
        shifts.sort("startTime", DESCENDING)
        shifts = list(shifts)

        return shifts