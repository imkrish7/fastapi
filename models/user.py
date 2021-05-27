from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
	name: str
	email: str
	password: str
	phoneNumber: str

class LoginUser(BaseModel):
	email: str
	password: str