from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_account,
    delete_account,
    retrieve_account,
    update_account,
)
from app.server.models.account import (
    ErrorResponseModel,
    ResponseModel,
    AccountSchema,
    UpdateAccountModel,
)

router = APIRouter()

@router.post("/", response_description="Account data added into the database")
async def add_account_data(account: AccountSchema = Body(...)):
    account = jsonable_encoder(account)
    new_account = await add_account(account)
    return ResponseModel(new_account, "Account added successfully.") 


# @router.get("/{id}", response_description="account data retrieved")
# async def get_account_data(user_id: str):
#     account = await retrieve_account(user_id)
#     if account:
#         return ResponseModel(account, "account data retrieved successfully")
#     return ErrorResponseModel("Error", 404, "account doesn't exist")

# @router.put("/{id}")
# async def update_account_data(user_id: str, req: UpdateaccountModel = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_account = await update_accounts(user_id, req)
#     if updated_account:
#         return ResponseModel(
#             "account with user_id: {} update is successful".format(user_id),
#             "account updated successfully",
#         )
#     return ErrorResponseModel(
#         "An error occurred",
#         404,
#         "There was an error updating the account data.",
#     )
    
# @router.delete("/{id}", response_description="account data deleted from the database")
# async def delete_account_data(user_id: str):
#     deleted_account = await delete_account(user_id)
#     if deleted_account:
#         return ResponseModel(
#             "account with user_id: {} removed".format(user_id), 
#             "account deleted successfully"
#         )
#     return ErrorResponseModel(
#         "An error occurred", 404, "account with user_id {0} doesn't exist".format(user_id)
#     )


@router.get("/{username}", response_description="Account data retrieved")
async def get_account_data(username: str):
    account = await retrieve_account(username)
    if account:
        return ResponseModel(account, "Account data retrieved successfully")
    return ErrorResponseModel("Error", 404, "Account doesn't exist")

@router.put("/{username}")
async def update_account_data(username: str, req: UpdateAccountModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_account = await update_account(username, req)
    if updated_account:
        return ResponseModel(
            "Account with username: {} update is successful".format(username),
            "Account updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the account data.",
    )
    
@router.delete("/{username}", response_description="Account data deleted")
async def delete_account_data(username: str):
    deleted_account = await delete_account(username)
    if deleted_account:
        return ResponseModel(
            "Account with username: {} removed".format(username),
            "Account deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Account with username {0} doesn't exist".format(username)
    )