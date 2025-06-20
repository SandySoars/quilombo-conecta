import streamlit as st

def menu_inferior():
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 Início"):
            st.session_state["pagina"] = "feed"

    with col2:
        if st.button("👤 Perfil"):
            st.session_state["pagina"] = "perfil"
