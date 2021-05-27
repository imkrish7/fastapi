from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from config.jwtConfig import SECRET, ALGORITHM, ACCESS_TOKEN_EXPIRES_MINTUES

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=15)
	to_encode.update({ "exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
	return encoded_jwt
	

def decode_access_token(token):
	payload = jwt.decode(token, SECRET, algorithm=ALGORITHM)
	return payload

