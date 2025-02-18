from fastapi import HTTPException

def format_response(status_code: int = 200, status: str = 'success', message: str = 'Operation successful', data=None):
    return {"status_code": status_code, "status": status, "message": message, "data": data or []}

def raise_error(status_code: int = 500, message: str = 'Server error'):
    raise HTTPException(status_code=status_code, detail=format_response(status_code, "failed", message))