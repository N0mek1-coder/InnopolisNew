import requests
import streamlit as st

from api.client import get_error_message, get_recipe
from components.recipe_card import render_admin_actions, render_favorite_button


recipe_id = st.session_state.get("selected_recipe_id")

if recipe_id is None:
    st.info("Сначала выберите запись в каталоге.")
    st.page_link("pages/catalog.py", label="Перейти в каталог")
    st.stop()

try:
    response = get_recipe(recipe_id)
except requests.RequestException:
    st.error("Не удалось выполнить запрос к backend.")
    st.stop()

if not response.ok:
    st.error(get_error_message(response))
    st.stop()

recipe = response.json()

st.header(recipe["title"])

if recipe.get("image_url"):
    st.image(recipe["image_url"], width=500)

st.write(recipe.get("description", ""))
render_favorite_button(recipe, key_prefix="details")
render_admin_actions(recipe["id"], key_prefix="details")