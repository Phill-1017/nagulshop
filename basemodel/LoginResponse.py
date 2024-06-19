from pydantic import BaseModel
class LoginResponse(BaseModel):
    id: int
    username: str
    role: str
