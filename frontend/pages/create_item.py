import streamlit as st
import requests

from frontend.api.client import BACKEND_URL, upload_image


image_url = f"{BACKEND_URL}{recipe['photo_path']}"

st.title("Создание сущности")

name = st.text_input("Название")
description = st.text_area("Описание")

uploaded_file = st.file_uploader("Изображение")

if uploaded_file is not None:
    st.image(uploaded_file)

if st.button("Создать"):
    # 1. создаём сущность без изображения
    create_response = requests.post(
        f"{BACKEND_URL}/recipes",
        json={
            "name": name,
            "description": description,
        },
    )

    recipe = create_response.json()
    recipe_id = recipe["id"]

    # 2. загружаем изображение
    image_data = upload_image(uploaded_file)

    # 3. привязываем изображение к сущности
    requests.patch(
        f"{BACKEND_URL}/recipes/{recipe_id}",
        json={
            "photo_path": image_data["photo_path"],
        },
    )

    st.success("Сущность создана")

    st.image(image_data["image_url"])