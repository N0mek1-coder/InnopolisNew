from pydantic import BaseModel, ConfigDict, Field

class RecipeCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=200)
    instructions: str = Field(min_length=1, max_length=200)
    imageUrl: str = Field(min_length=1, max_length=200)
    cookTime: int
    difficulty: str = Field(min_length=1, max_length=200)
    userId: int


class RecipeUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, min_length=1, max_length=200)
    instructions: str | None = Field(None, min_length=1, max_length=200)
    imageUrl: str | None = Field(None, min_length=1, max_length=200)
    cookTime: int | None
    difficulty: str | None = Field(None, min_length=1, max_length=200)
    userId: int | None


class RecipeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    instructions: str
    imageUrl: str
    cookTime: int
    difficulty: str
    userId: int
