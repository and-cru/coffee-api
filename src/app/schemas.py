from typing import List, Optional
from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    coffee: Optional[str] = None
    brew_time: Optional[float] = 0.0
    taste_notes: Optional[str] = None
    tags: Optional[str] = None

class RecipeCreate(ItemBase):
    pass

class Recipe(RecipeBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class BrewerBase(BaseModel):
    name: str

class BrewerCreate(BrewerBase):
    name: str

class Brewer(BrewerBase):
    id: int
    recipes: List[Recipe] = []
    class Config:
        orm_mode = True
