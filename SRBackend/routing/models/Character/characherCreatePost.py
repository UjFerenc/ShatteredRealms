from pydantic import BaseModel


class CharacterCreatePost(BaseModel):
    charName: str