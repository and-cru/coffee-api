from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship

from app.database import Base


class Brewer(Base):
    __tablename__ = "brewer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    recipes = relationship("Recipe", back_populates="brewer")


class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    coffee = Column(String, index=True)
    description = Column(String, index=True)
    brew_time = Column(Float, index=True)
    taste_notes = Column(String, index=True)
    tags = Column(String, index=True)
    brewer_id = Column(Integer, ForeignKey("brewer.id"))

    brewer = relationship("Brewer", back_populates="recipe")