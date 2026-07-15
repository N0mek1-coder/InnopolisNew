from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.recipe import Recipe
from app.repositories.recipe_repository import RecipeRepository
from app.schemas.recipe import RecipeCreate, RecipeUpdate


class RecipeService:

    def __init__(self, db: Session):
        self.repository = RecipeRepository(db)

    def create_recipe(self, schema: RecipeCreate) -> Recipe:
        recipe = Recipe(**schema.model_dump())

        return self.repository.create(recipe)

    def get_recipes(self) -> list[Recipe]:
        return self.repository.get_all()

    def get_recipe(self, recipe_id: int) -> Recipe:
        recipe = self.repository.get_by_id(recipe_id)

        if recipe is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recipe not found",
            )

        return recipe

    def update_recipe(
        self,
        recipe_id: int,
        schema: RecipeUpdate,
    ) -> Recipe:

        recipe = self.get_recipe(recipe_id)

        if schema.title is None and schema.author is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one field must be provided",
            )

        if schema.title is not None:
            recipe.title = schema.title

        if schema.author is not None:
            recipe.author = schema.author

        return self.repository.update(recipe)

    def delete_recipe(self, recipe_id: int) -> None:
        recipe = self.get_recipe(recipe_id)

        self.repository.delete(recipe)