from fastapi import status, Response
from fastapi.responses import JSONResponse

def response_200(data=None):
	return JSONResponse(status_code=200, content={"success": True, "data": data})

def response_201(data=None):
	return JSONResponse(status_code=201, content={"success": True, "msg": "document created", "data": data})

def response_400(data=None):
	return JSONResponse(status_code=400, content={"success": False, "msg": "User error"})

def response_401(data=None):
	return JSONResponse(status_code=401, content={"success": False,"msg": "Unauthorized"})

def response_404(data=None):
	return JSONResponse(status_code=404, content={"success": False,"msg": "Document not found"})

def response_403(data=None):
	return JSONResponse(status_code=403, content={"success": False, "msg": "Forbidden"})

def response_500(data=None):
	return JSONResponse(status_code=500, content={ "success": False, "msg": "Internal server error"})