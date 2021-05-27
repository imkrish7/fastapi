from models.email import EmailSchema
from models.contact import ContactSchema
from urllib.parse import uses_relative
from pymongo import MongoClient;
from services.bycrypt import hash_password, verify_password
from pymongo.pool import _configured_socket
MONGO_URI = "mongodb+srv://krishna:abc123@cluster0.uirfi.mongodb.net/bookscrib?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["bookscrib"]


def get_user(user):
	userCol = db.user
	try:
		isUser = userCol.find_one({"email": user["email"]})
		if isUser:
			return isUser
		else:
			return None
	except Exception as e:
		print(e)
		return None

def add_user(user):
	email = user["email"]
	name = user["name"]
	phoneNumber = user["phoneNumber"]
	password = hash_password(user["password"])
	try:
		print(db)
		if db:
			userCol = db["user"]
			
			if userCol:
				userCol.insert_one({"email": email, "name":name, "phoneNumber": phoneNumber, "password": password});
				return True
			else:
				return False
		else:
			return False
	except Exception as e:
		print(e)
		return False

async def add_email(data):
	try:
		if db:
			emailCol = db["email"]
			if emailCol:
				data =emailCol.insert_one({"email": data['email'], 'isSignedUp': True})
				return True
			else:
				return False
		else:
			return False
	except Exception as e:
		print(e)
		return False

def add_contact(contact: ContactSchema):
	
	try:
		if db:
			contactCollection = db['contact']
			if contactCollection:
				contactCollection.insert_one({"email": contact["email"], "phoneNumber": contact["phoneNumber"], "name": contact["name"], "message": contact["message"]}, upsert=True)
				return True
			else:
				return False
		return False
	except Exception as e:
		print(e)
		return False