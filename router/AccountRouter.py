from fastapi import APIRouter,HTTPException
from sqlalchemy.exc import SQLAlchemyError
from starlette import status
from starlette.responses import JSONResponse

import repository.repository
from basemodel.AccountRequest import AccountRequest
from model.Account import Account
from repository.repository import register, login

from basemodel.LoginRequest import LoginRequest
from basemodel.LoginResponse import LoginResponse


accountRouter = APIRouter()

@accountRouter.post("/register")
async def registerAccount(account: AccountRequest):
    try:
        await register(account)
        return JSONResponse(status_code=200, content={'message': 'Success'})
    except SQLAlchemyError as db_error:
        print(db_error)
        return JSONResponse(content={"message": "duplicate"}, status_code=401)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"}, status_code=500)


@accountRouter.post("/login", response_model=LoginResponse)
async def login(loginRequest: LoginRequest):
    try:
        acc = await repository.repository.login(loginRequest)
        if acc is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong username or password")

        # Ensure that `acc` includes id, username, and role
        return LoginResponse(id=acc.id, username=acc.username, role=acc.role)
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred")