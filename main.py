from fastapi import Depends, FastAPI, HTTPException
from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# health checker
@app.get("/health", status_code=200 )
async def root():
    return {"message": "I am healthy"}

# Basic crud operations
@app.post("/brewers/", response_model=schemas.Brewer)
def create_brewer(brewer: schemas.BrewerCreate, db: Session = Depends(get_db)):
    db_user = crud.get_brewer_by_name(db, name=brewer.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Brewer already registered")
    return crud.create_brewer(db=db, brewer=brewer)

@app.get("/brewers/", response_model=List[schemas.Brewer])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    brewers = crud.get_brewers(db, skip=skip, limit=limit)
    return brewers

@app.get("/brewers/{brewer_id}", response_model=schemas.Brewer)
def read_brewer(brewer_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_brewer(db, brewer_id=brewer_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Brewer not found")
    return db_user

@app.post("/brewers/{brewer_id}/recipes/", response_model=schemas.Recipe)
def create_recipe_for_brewer(
    brewer_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(get_db)
):
    return crud.create_brewer_recipe(db=db, recipe=recipe, brewer_id=brewer_id)

@app.get("/recipes/", response_model=List[schemas.Recipe])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    return recipes