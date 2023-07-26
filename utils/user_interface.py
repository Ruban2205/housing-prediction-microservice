import streamlit as st



def load_css_file(css_file_path):
    with open(css_file_path, encoding='UTF-8') as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


