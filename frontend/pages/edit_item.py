import requests
import streamlit as st

from api.client import get_error_message, get_recipe, update_recipe
from auth.state import require_admin


require_admin()
st.header("Редактирование записи")

recipe_id = st.session_state.get("edit_recipe_id")

if recipe_id is None:
    st.info("Сначала выберите запись для редактирования.")
    st.stop()

try:
    recipe_response = get_recipe(recipe_id)
except requests.RequestException:
    st.error("Не удалось получить запись с backend.")
    st.stop()

if not recipe_response.ok:
    st.error(get_error_message(recipe_response))
    st.stop()

recipe = recipe_response.json()

with st.form(f"edit_recipe_form_{recipe_id}"):
    title = st.text_input("Название", value=recipe["title"])
    short_description = st.text_area(
        "Краткое описание",
        value=recipe.get("short_description", ""),
    )
    description = st.text_area(
        "Полное описание",
        value=recipe.get("description", ""),
    )
    image_url = st.text_input(
        "Ссылка на изображение",
        value=recipe.get("image_url") or "",
    )
    submitted = st.form_submit_button("Сохранить")

if submitted:
    if not title.strip():
        st.error("Укажите название.")
        st.stop()

    payload = {
        "title": title.strip(),
        "short_description": short_description.strip(),
        "description": description.strip(),
        "image_url": image_url.strip() or None,
    }

    try:
        response = update_recipe(recipe_id, payload)
    except requests.RequestException:
        st.error("Не удалось выполнить запрос к backend.")
        st.stop()

    if response.ok:
        st.session_state["selected_recipe_id"] = recipe_id
        st.switch_page("pages/details.py")
    else:
        st.error(get_error_message(response))