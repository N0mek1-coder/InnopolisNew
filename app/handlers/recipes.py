from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.recipe import RecipeCreate, RecipeResponse, RecipeUpdate
from app.services.recipe_service import RecipeService

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)


def get_recipe_service(
    db: Session = Depends(get_db),
) -> RecipeService:
    return RecipeService(db)


@router.post(
    "/",
    response_model=RecipeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_recipe(
    schema: RecipeCreate,
    service: RecipeService = Depends(get_recipe_service),
):
    return service.create_recipe(schema)


@router.get(
    "/",
    response_model=list[RecipeResponse],
)
def get_recipes(
    service: RecipeService = Depends(get_recipe_service),
):
    return service.get_recipes()


@router.get(
    "/{recipe_id}",
    response_model=RecipeResponse,
)
def get_recipe(
    recipe_id: int,
    service: RecipeService = Depends(get_recipe_service),
):
    return service.get_recipe(recipe_id)


@router.patch(
    "/{recipe_id}",
    response_model=RecipeResponse,
)
def update_recipe(
    recipe_id: int,
    schema: RecipeUpdate,
    service: RecipeService = Depends(get_recipe_service),
):
    return service.update_recipe(recipe_id, schema)


@router.delete(
    "/{recipe_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_recipe(
    recipe_id: int,
    service: RecipeService = Depends(get_recipe_service),
) -> None:
    service.delete_recipe(recipe_id)