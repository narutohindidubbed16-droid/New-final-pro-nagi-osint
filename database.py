# ==========================================
# 📌 MongoDB Database Handler (With Referral System)
# ==========================================

from pymongo import MongoClient
from config import MONGO_URL, DB_NAME
from datetime import datetime

# -----------------------------
# Connect Database
# -----------------------------
client = MongoClient(MONGO_URL)
db = client[DB_NAME]

users = db["users"]

# -----------------------------
# Create User
# -----------------------------
def create_user(user_id, username, name, referrer=None):
    user = users.find_one({"user_id": user_id})
    if not user:
        data = {
            "user_id": user_id,
            "username": username,
            "name": name,
            "credits": 10,
            "referrer": referrer,
            "referrals": 0,
            "joined": datetime.now()
        }
        users.insert_one(data)
        return True
    return False


# -----------------------------
# Add Referral to Referrer
# -----------------------------
def add_referral(referrer_id):
    users.update_one(
        {"user_id": referrer_id},
        {"$inc": {"referrals": 1, "credits": 1}}  # Earn 1 credit per referral
    )


# -----------------------------
# Get Credits
# -----------------------------
def get_credits(user_id):
    user = users.find_one({"user_id": user_id})
    if not user:
        return 0
    return user.get("credits", 0)


# -----------------------------
# Decrease Credit
# -----------------------------
def decrease_credit(user_id, amount=1):
    users.update_one(
        {"user_id": user_id},
        {"$inc": {"credits": -amount}}
    )


# -----------------------------
# Add Credit (Admin)
# -----------------------------
def add_credit(user_id, amount):
    users.update_one(
        {"user_id": user_id},
        {"$inc": {"credits": amount}}
    )


# -----------------------------
# Total Users
# -----------------------------
def total_users():
    return users.count_documents({})


# -----------------------------
# Get All Users
# -----------------------------
def get_all_users():
    return users.find({})
