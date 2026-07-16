import streamlit as st

from auth.state import is_admin


st.set_page_config(
    page_title="Каталог",
    page_icon="📚",
    layout="wide",
)

pages = {
    "Каталог": [
        st.Page(
            "pages/catalog.py",
            title="Каталог",
            icon=":material/store:",
            url_path="catalog",
            default=True,
        ),
        st.Page(
            "pages/details.py",
            title="Подробнее",
            icon=":material/article:",
            url_path="details",
        ),
    ],
    "Пользователь": [
        st.Page(
            "pages/favorites.py",
            title="Избранное",
            icon=":material/favorite:",
            url_path="favorites",
        ),
        st.Page(
            "pages/profile.py",
            title="Профиль",
            icon=":material/person:",
            url_path="profile",
        ),
    ],
    "Авторизация": [
        st.Page(
            "pages/login.py",
            title="Вход",
            icon=":material/login:",
            url_path="login",
        ),
        st.Page(
            "pages/registration.py",
            title="Регистрация",
            icon=":material/person_add:",
            url_path="registration",
        ),
    ],
}

if is_admin():
    pages["Администратор"] = [
        st.Page(
            "pages/create_recipe.py",
            title="Создать запись",
            icon=":material/add:",
            url_path="create-recipe",
        ),
        st.Page(
            "pages/edit_recipe.py",
            title="Редактировать запись",
            icon=":material/edit:",
            url_path="edit-recipe",
        ),
    ]

navigation = st.navigation(pages)
navigation.run()