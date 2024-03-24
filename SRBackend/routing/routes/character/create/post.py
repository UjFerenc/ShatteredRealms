from fastapi import Response, Depends

from database.main import session
from database.models.User.playercharacters import PlayerCharacter
from sqlalchemy import exc

from dependencies.Authentication.getCurrentUser import get_current_user
from routing.models.Character.characherCreatePost import CharacterCreatePost

tags = ['character']

def handler(data: CharacterCreatePost, response: Response, user = Depends(get_current_user)):
    playerCharacter = PlayerCharacter(data.charName)
    user.characters.append(playerCharacter)

    try:
        session.commit()
        return playerCharacter
    except exc.SQLAlchemyError as e:
        session.rollback()
        response.status_code = 500
        return str(e.__dict__['orig'])
