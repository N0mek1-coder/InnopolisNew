from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, Request, UploadFile, status

from app.schemas.image import ImageUploadResponse


router = APIRouter(
    prefix="/images",
    tags=["images"],
)

MEDIA_DIR = Path(__file__).resolve().parent.parent / "media"
RECIPE_IMAGES_DIR = MEDIA_DIR / "recipes"

RECIPE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "/upload",
    response_model=ImageUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_image(
    request: Request,
    file: UploadFile = File(...),
) -> ImageUploadResponse:
    extension = Path(file.filename or "").suffix

    content = await file.read()
    await file.close()

    filename = f"{uuid4()}{extension}"
    image_path = RECIPE_IMAGES_DIR / filename

    image_path.write_bytes(content)

    photo_path = f"/media/recipes/{filename}"

    image_url = request.url_for(
        "media",
        path=f"recipes/{filename}",
    )

    return ImageUploadResponse(
        filename=filename,
        photo_path=photo_path,
        image_url=str(image_url),
    )