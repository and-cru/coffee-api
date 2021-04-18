from sqlalchemy.orm import Session
from . import models, schemas

def get_brewer(db: Session, brewer_id: int):
    return db.query(models.Brewer).filter(models.Brewer.id == brewer_id).first()

def get_brewer_by_name(db: Session, name: str):
    return db.query(models.Brewer).filter(models.Brewer.name == name).first()

def get_brewer_by_id(db: Session, brewer_id: id):
    return db.query(models.Brewer).filter(models.Brewer.id == brewer_id).first()

def get_brewers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brewer).offset(skip).limit(limit).all()

def create_brewer(db: Session, brewer: schemas.BrewerCreate):
    db_brewer = models.Brewer(name=brewer.name)
    db.add(db_brewer)
    db.commit()
    db.refresh(db_brewer)
    return db_brewer

def delete_brewer(db: Session, brewer_id: int):
    db_brewer = db.query(models.Brewer).filter(models.Brewer.id == brewer_id).first()
    db.delete(db_brewer)
    db.commit()
    return {"message": "Successfully deleted user"}

def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def create_brewer_recipe(db: Session, recipe: schemas.RecipeCreate, brewer_id: int):
    db_recipe = models.Recipe(**recipe.dict(), brewer_id=brewer_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete_brewer_recipe(db: Session, recipe_id: int, brewer_id: int):
    db_recipe = models.Recipe(id=recipe_id)
    db.delete(db_recipe)
    db.commit()
    return db_recipe