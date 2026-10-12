import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="VALORACIÓN CANTERA — Racing Club Ferrol",
    page_icon="⚽",
    layout="wide",
)

# Quita el padding por defecto de Streamlit para que el dashboard
# ocupe todo el ancho, sin marco extra alrededor.
st.markdown(
    """
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Se lee en cada ejecución (sin caché) para que, al subir un dashboard.html
# nuevo, la app lo muestre en cuanto Streamlit se redespliegue.
html_path = Path(__file__).parent / "dashboard.html"
html_content = html_path.read_text(encoding="utf-8")

# height fijo con scroll interno: el dashboard cambia de alto según la
# pestaña (Valoración general / Pliegues / PHV) y al abrir una ficha.
components.html(html_content, height=2600, scrolling=True)
