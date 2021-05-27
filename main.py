from models.email import EmailSchema
from models.contact import ContactSchema
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from models.user import UserSchema, LoginUser
from db import add_user, get_user, add_email
from services.bycrypt import verify_password
from services.jwt import create_access_token
from services.responses import *

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=['*']
)

@app.post("/signup")
async def signup(user: UserSchema):
	result = add_user(user)
	if result:
		return response_200()
	else:
		return response_400()

@app.post("/login")
async def login(user: LoginUser):

	isUser = get_user(user);
	if isUser:
		print(isUser)
		check_password = verify_password(user.password, isUser["password"])
		if check_password:
			payload = {"email": isUser["email"], "name": isUser["name"]}
			token = create_access_token(payload)
			return response_200({ "token": token})
		else:
			return response_403()

@app.post("/get_started")
async def get_started(request: Request):
	# print(await request.json())
	data = await request.json()
	result = await add_email(data)
	if result:
		return response_200()
	else:
		return response_500()

@app.post('/contact')
async def add_contact(contact: ContactSchema):
	result = add_contact(contact)
	if result:
		return response_200()
	else:
		return response_500()
