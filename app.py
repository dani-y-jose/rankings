import os

import streamlit as st
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]


@st.cache_resource
def get_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)


supabase = get_supabase()

st.set_page_config(page_title="Ranking", layout="wide")
st.title("Ranking")

TABLES = {
    "Categories": "categories",
    "Places": "places",
    "Reviewers": "reviewers",
    "Products": "products",
    "Features": "features",
    "Reviews": "reviews",
    "Stars": "stars",
}

tab_labels = list(TABLES.keys())
tabs = st.tabs(tab_labels)

for tab, (label, table_name) in zip(tabs, TABLES.items()):
    with tab:
        if table_name == "products":
            with st.form("add_product", clear_on_submit=True):
                st.subheader("Add Product")
                name = st.text_input("Product Name")
                categories = supabase.table("categories").select("id, name").execute().data
                category_options = {c["name"]: c["id"] for c in categories} if categories else {}
                category = st.selectbox(
                    "Category",
                    options=list(category_options.keys()),
                    index=None,
                    placeholder="Select a category...",
                )
                submitted = st.form_submit_button("Add")
                if submitted and name:
                    row = {"name": name}
                    if category:
                        row["category_id"] = category_options[category]
                    supabase.table("products").insert(row).execute()
                    st.success(f"Product **{name}** added!")
                    st.rerun()

        response = supabase.table(table_name).select("*").execute()
        data = response.data
        if data:
            st.dataframe(data, use_container_width=True)
        else:
            st.info(f"No data in **{table_name}** yet.")
