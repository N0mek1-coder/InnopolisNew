import requests
import streamlit as st

from api.client import get_error_message, get_favorites
from auth.state import require_login
from components.recipe_card import render_recipe_card


require_login()
st.header("Избранное")

try:
    response = get_favorites()
except requests.RequestException:
    st.error("Не удалось выполнить запрос к backend.")
    st.stop()

if not response.ok:
    st.error(get_error_message(response))
    st.stop()

recipes = response.json()

if not recipes:
    st.info("В избранном пока ничего нет.")
    st.stop()

for recipe in recipes:
    render_recipe_card(recipe)