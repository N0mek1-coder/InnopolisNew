from sqlalchemy.orm import Session

from app.models.recipe import Recipe


class RecipeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, recipe: Recipe) -> Recipe:
        return self._upsert(recipe)

    def update(self, recipe: Recipe) -> Recipe:
        return self._upsert(recipe)

    def _upsert(self, recipe: Recipe) -> Recipe:
        self.db.add(recipe)
        self.db.commit()
        self.db.refresh(recipe)

        return recipe

    def get_all(self) -> list[Recipe]:
        return self.db.query(Recipe).all()

    def get_by_id(
        self,
        recipe_id: int,
    ) -> Recipe | None:

        return (
            self.db.query(Recipe)
            .filter(Recipe.id == recipe_id)
            .first()
        )

    def delete(self, recipe: Recipe) -> None:
        self.db.delete(recipe)
        self.db.commit()

def update(self, recipe: Recipe) -> Recipe:
    return self._upsert(recipe)