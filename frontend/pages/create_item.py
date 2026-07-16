import requests
import streamlit as st

from api.client import create_recipe, get_error_message
from auth.state import require_admin


require_admin()
st.header("Новая запись")

with st.form("create_recipe_form"):
    title = st.text_input("Название")
    short_description = st.text_area("Краткое описание")
    description = st.text_area("Полное описание")
    image_url = st.text_input("Ссылка на изображение")
    submitted = st.form_submit_button("Создать")

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
        response = create_recipe(payload)
    except requests.RequestException:
        st.error("Не удалось выполнить запрос к backend.")
        st.stop()

    if response.status_code in (200, 201):
        created_recipe = response.json()
        st.session_state["selected_recipe_id"] = created_recipe["id"]
        st.switch_page("pages/details.py")
    else:
        st.error(get_error_message(response))