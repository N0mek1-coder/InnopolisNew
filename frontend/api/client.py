from typing import Any

import requests


BACKEND_URL = "http://127.0.0.1:8000"


def upload_image(uploaded_file: Any) -> dict:
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type,
        )
    }

    response = requests.post(
        f"{BACKEND_URL}/images/upload",
        files=files,
    )

    return response.json()