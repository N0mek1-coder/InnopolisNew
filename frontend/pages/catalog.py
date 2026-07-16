import requests
import streamlit as st

from api.client import get_error_message, get_recipes
from auth.state import is_admin
from components.recipe_card import render_recipe_card


st.header("Каталог")

if is_admin():
    if st.button("Создать запись"):
        st.switch_page("pages/create_recipe.py")

try:
    response = get_recipes()
except requests.RequestException:
    st.error("Backend недоступен. Проверьте запуск FastAPI.")
    st.stop()

if not response.ok:
    st.error(get_error_message(response))
    st.stop()

recipes = response.json()

if not recipes:
    st.info("В каталоге пока нет записей.")
    st.stop()

columns = st.columns(3)

for index, recipe in enumerate(recipes):
    with columns[index % 3]:
        render_recipe_card(recipe)