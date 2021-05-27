from typing import Optional
from pydantic import BaseModel

class ContactSchema(BaseModel):
	name: str
	phoneNumber: str
	email: str
	message: str