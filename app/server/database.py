import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.facebook_storage

account_collection = database.get_collection("formatted_streams")

# Add this after your database initialization
async def init_db():
    await account_collection.create_index("username", unique=True)
    # await account_collection.create_index("user_id", unique=True)

# helpers

# Update the helper function
def account_helper(accounts) -> dict:
    return {
        "id": str(accounts["_id"]),
        # "user_id": accounts["user_id"],  # Add new field
        "name": accounts["name"],
        "username": accounts["username"],
        "password": accounts["password"],
        "team": accounts["team"],
        "is_short_term": accounts["is_short_term"],
        "start_date": accounts.get("start_date", None),  # Optional field
        "end_date": accounts.get("end_date", None),      # Optional field
        "education": accounts.get("education", None),     # Optional field
        "is_helpdesk": accounts["is_helpdesk"],
        "is_admin": accounts.get("is_admin", False)      # Optional field with default False
    }
# # Update the add_account function to validate required fields
# async def add_account(account_data: dict) -> dict:
#     # Validate required fields
#     required_fields = ["user_id", "name", "username", "password", "team", "is_short_term", "is_helpdesk"]  # Add user_id
#     for field in required_fields:
#         if field not in account_data:
#             return None
            
#     account = await account_collection.insert_one(account_data)
#     new_account = await account_collection.find_one({"_id": account.inserted_id})
#     return account_helper(new_account)


# # Retrieve a account with matching user_id
# async def retrieve_account(user_id: str) -> dict:
#     account = await account_collection.find_one({"user_id": user_id})
#     if account:
#         return account_helper(account)
#     return None

# # Update a account with matching ID and user_id
# async def update_accounts(id: str, user_id: str, data: dict):
#     if len(data) < 1:
#         return False
    
#     account = await account_collection.find_one({
#         "_id": ObjectId(id),
#         "user_id": user_id
#     })
    
#     if account:
#         updated_account = await account_collection.update_one(
#             {"_id": ObjectId(id), "user_id": user_id},
#             {"$set": data}
#         )
#         if updated_account.modified_count > 0:
#             return True
#     return False

# # Update a account with matching user_id
# async def update_accounts(user_id: str, data: dict):
#     if len(data) < 1:
#         return False
    
#     account = await account_collection.find_one({"user_id": user_id})
    
#     if account:
#         updated_account = await account_collection.update_one(
#             {"user_id": user_id},
#             {"$set": data}
#         )
#         if updated_account.modified_count > 0:
#             return True
#     return False


# # Delete a account with matching user_id
# async def delete_account(user_id: str):
#     account = await account_collection.find_one({"user_id": user_id})
#     if account:
#         await account_collection.delete_one({"user_id": user_id})
#         return True
#     return False


async def add_account(account_data: dict) -> dict:
    # Update required fields to use username instead of user_id
    required_fields = ["username", "name", "password", "team", "is_short_term", "is_helpdesk"]
    for field in required_fields:
        if field not in account_data:
            return None
            
    account = await account_collection.insert_one(account_data)
    new_account = await account_collection.find_one({"_id": account.inserted_id})
    return account_helper(new_account)

async def retrieve_account(username: str) -> dict:
    account = await account_collection.find_one({"username": username})
    if account:
        return account_helper(account)
    return None

async def update_account(username: str, data: dict):
    if len(data) < 1:
        return False
    
    # Remove username from update data if present
    if "username" in data:
        del data["username"]
        
    account = await account_collection.find_one({"username": username})
    
    if account:
        updated_account = await account_collection.update_one(
            {"username": username},
            {"$set": data}
        )
        if updated_account.modified_count > 0:
            return True
    return False

async def delete_account(username: str):
    account = await account_collection.find_one({"username": username})
    if account:
        await account_collection.delete_one({"username": username})
        return True
    return False