from fastapi import HTTPException, Depends

from dependencies.Authentication.getCurrentUser import get_current_user

async def is_admin(user = Depends(get_current_user)):
    if not any(x.name == "admin" for x in user.roles):
        raise HTTPException(status_code=401, detail='UNAUTHORISED_REQUEST')
    return True