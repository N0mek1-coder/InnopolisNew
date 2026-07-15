from app.database import Base, SessionLocal, engine
from app.models.recipe import Recipe
from app.repositories.recipe_repository import RecipeRepository

Base.metadata.create_all(bind=engine)

db = SessionLocal()

repository = RecipeRepository(db)

recipe = Recipe(
    title="Высоконагруженные приложения",
    author="Мартин Клеппман",
)

repository.create(recipe)

recipes = repository.get_all()

for recipe in recipes:
    print(recipe.id, recipe.title, recipe.author)

db.close()