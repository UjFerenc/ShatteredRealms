from fastapi import HTTPException, Depends
from fastapi.security.http import HTTPBearer

from database.models.User.user import User
from database.main import session

get_bearer_token = HTTPBearer(auto_error=False)

async def get_current_user(token: str = Depends(get_bearer_token)):
    if not token:
        raise HTTPException(status_code=400, detail='Authorization header not found!')
    user = session.query(User).filter_by(loginToken=token.credentials).first()
    if user is None:
        raise HTTPException(status_code=400, detail='Invalid authorization token!')

    return user