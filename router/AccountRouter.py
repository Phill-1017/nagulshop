import repository.repository
from fastapi import APIRouter,HTTPException
from sqlalchemy.exc import SQLAlchemyError
from starlette import status
from starlette.responses import JSONResponse
from basemodel.AccountRequest import AccountRequest
from repository.repository import register
from basemodel.LoginRequest import LoginRequest
from basemodel.LoginResponse import LoginResponse

accountRouter = APIRouter()
@accountRouter.post("/register")
def registerAccount(account: AccountRequest):
    try:
        register(account)
        return JSONResponse(status_code=200, content={'message': 'Success'})
    except SQLAlchemyError as db_error:
        print(db_error)
        return JSONResponse(content={"message": "duplicate"}, status_code=401)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"}, status_code=500)

@accountRouter.post("/login", response_model=LoginResponse)
def loginAccount(loginRequest: LoginRequest):
    try:
        acc = repository.repository.login(loginRequest)
        if acc is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong username or password")

        return LoginResponse(id=acc.id, username=acc.username, role=acc.role)
    except SQLAlchemyError as db_error:
        print(db_error)
        return JSONResponse(content={"message": "db error: failed login"}, status_code=401)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"}, status_code=500)