from pydantic import BaseModel


class Bookmark(BaseModel):
    name: str
    url: str
    type: int

class Category(BaseModel):
    name: str