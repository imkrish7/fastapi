from bcrypt import checkpw, hashpw, gensalt


def hash_password(password:str):
	hashedpw = hashpw(password.encode('utf-8'), gensalt())
	return hashedpw

def verify_password(password: str, hashedpw: str):
	isSame = checkpw(password.encode('utf-8'), hashedpw)
	return isSame