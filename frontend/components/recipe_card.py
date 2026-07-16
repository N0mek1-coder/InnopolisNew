import requests
import streamlit as st

from api.client import (
    add_favorite,
    delete_recipe,
    get_error_message,
    remove_favorite,
)
from auth.state import is_admin, is_authenticated


def render_favorite_button(recipe: dict, key_prefix: str) -> None:
    if not is_authenticated():
        st.caption("Войдите, чтобы добавить запись в избранное.")
        return

    recipe_id = recipe["id"]
    is_favorite = recipe.get("is_favorite", False)
    button_text = "Убрать из избранного" if is_favorite else "В избранное"

    if st.button(button_text, key=f"{key_prefix}_favorite_{recipe_id}"):
        try:
            if is_favorite:
                response = remove_favorite(recipe_id)
            else:
                response = add_favorite(recipe_id)
        except requests.RequestException:
            st.error("Не удалось выполнить запрос к backend.")
            return

        if response.ok:
            st.rerun()
        else:
            st.error(get_error_message(response))


def render_admin_actions(recipe_id: int, key_prefix: str) -> None:
    if not is_admin():
        return

    edit_column, delete_column = st.columns(2)

    if edit_column.button(
        "Редактировать",
        key=f"{key_prefix}_edit_{recipe_id}",
    ):
        st.session_state["edit_recipe_id"] = recipe_id
        st.switch_page("pages/edit_recipe.py")

    if delete_column.button(
        "Удалить",
        key=f"{key_prefix}_delete_{recipe_id}",
        type="primary",
    ):
        try:
            response = delete_recipe(recipe_id)
        except requests.RequestException:
            st.error("Не удалось выполнить запрос к backend.")
            return

        if response.ok:
            st.success("Запись удалена.")
            st.switch_page("pages/catalog.py")
        else:
            st.error(get_error_message(response))


def render_recipe_card(recipe: dict) -> None:
    recipe_id = recipe["id"]

    with st.container(border=True):
        if recipe.get("image_url"):
            st.image(recipe["image_url"], use_container_width=True)
        else:
            st.info("Изображение не добавлено")

        st.subheader(recipe["title"])
        st.write(recipe.get("short_description", ""))

        render_favorite_button(recipe, key_prefix="card")

        if st.button("Подробнее", key=f"card_details_{recipe_id}"):
            st.session_state["selected_recipe_id"] = recipe_id
            st.switch_page("pages/details.py")

        render_admin_actions(recipe_id, key_prefix="card")