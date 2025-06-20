import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Funções de login e cadastro
from user_auth import login_user, cadastrar_user

# Funções do app principal
from main_app import (
    feed_principal,
    criar_demanda,
    visualizar_por_categoria,
    pagina_perfil
)

# Configuração da página (deve ser a 1ª chamada do Streamlit)
st.set_page_config(page_title="Quilombo Conecta", layout="centered")

# ----- Inicialização de variáveis de estado -----
if "pagina" not in st.session_state:
    st.session_state["pagina"] = "feed"

if "tela_cadastro" not in st.session_state:
    st.session_state["tela_cadastro"] = False

# ----- LOGO E BOAS-VINDAS -----
def img_to_bytes(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def mostrar_logo():
    logo = Image.open("logo.png")
    logo_base64 = img_to_bytes(logo)
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{logo_base64}" width="200" />
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <h2 style='text-align: center; color: #4B4B4B;'>
            Bem-vindo ao Quilombo Conecta,<br>
            <em>a voz da nossa comunidade.</em>
        </h2>
        """,
        unsafe_allow_html=True,
    )

# Mostrar logo antes do login
if "usuario_logado" not in st.session_state or not st.session_state["usuario_logado"]:
    mostrar_logo()

# ----- VERIFICA SE USUÁRIO ESTÁ LOGADO -----
if "usuario_logado" in st.session_state and st.session_state["usuario_logado"]:

    # Roteamento entre páginas
    if st.session_state["pagina"] == "feed":
        feed_principal()
    elif st.session_state["pagina"] == "criar":
        criar_demanda()
    elif st.session_state["pagina"] == "filtrar_categoria":
        visualizar_por_categoria()
    elif st.session_state["pagina"] == "visualizar":
        st.write("🔎 Aqui será a visualização de todas as demandas.")
    elif st.session_state["pagina"] == "reunioes":
        st.write("📅 Aqui você verá todas as reuniões agendadas.")
    elif st.session_state["pagina"] == "eventos":
        st.write("🎉 Aqui você verá os eventos comunitários.")
    elif st.session_state["pagina"] == "comunicados":
        st.write("📢 Aqui você verá os comunicados importantes.")
    elif st.session_state["pagina"] == "perfil":  # ✅ corrigido: agora está dentro do bloco do usuário logado
        pagina_perfil()

# ----- TELA DE LOGIN / CADASTRO -----
else:

    def toggle_tela():
        st.session_state["tela_cadastro"] = not st.session_state["tela_cadastro"]

    if not st.session_state["tela_cadastro"]:
        st.subheader("Login")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            login_user(email, senha)
        if st.button("Cadastrar"):
            toggle_tela()
    else:
        st.subheader("Cadastro")
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        senha = st.text_input("Senha", type="password")
        comunidade = st.text_input("Comunidade")
        if st.button("Cadastrar"):
            cadastrar_user(nome, email, telefone, senha, comunidade)
        if st.button("Voltar para Login"):
            toggle_tela()
