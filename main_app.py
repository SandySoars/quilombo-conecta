import streamlit as st
from crud_demandas import salvar_demanda, buscar_demandas_por_categoria
from PIL import Image
import io

from ui_components import menu_inferior

# ----------------------------
# PARTE 1: Tela principal com cards
# ----------------------------
def feed_principal():
    st.title("📢 Feed de Demandas")

    with st.container():
        st.markdown("### 🗂️ Demandas por categoria")
        categorias = ["Educação", "Transporte", "Saúde", "Infraestrutura", "Cultura"]
        col1, col2 = st.columns(2)
        for i, categoria in enumerate(categorias):
            with (col1 if i % 2 == 0 else col2):
                if st.button(f"📌 {categoria}"):
                    st.session_state["pagina"] = "filtrar_categoria"
                    st.session_state["categoria_selecionada"] = categoria

        st.markdown("---")
        colA, colB = st.columns(2)
        with colA:
            if st.button("🔍 Visualizar todas as demandas"):
                st.session_state["pagina"] = "visualizar"
        with colB:
            if st.button("➕ Criar nova demanda"):
                st.session_state["pagina"] = "criar"

    st.markdown("---")
    with st.container():
        st.markdown("### 📰 Novidades")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📅 Reuniões"):
                st.session_state["pagina"] = "reunioes"
        with col2:
            if st.button("🎉 Eventos"):
                st.session_state["pagina"] = "eventos"
        with col3:
            if st.button("📢 Comunicados"):
                st.session_state["pagina"] = "comunicados"

    menu_inferior()

# ----------------------------
# PARTE 2: Formulário de criação de demanda
# ----------------------------
def criar_demanda():
    st.title("➕ Criar Nova Demanda")

    titulo = st.text_input("Título da Demanda")
    descricao = st.text_area("Descrição da Demanda")
    categoria = st.selectbox("Categoria", ["Educação", "Transporte", "Saúde", "Infraestrutura", "Cultura"])
    imagem = st.file_uploader("Anexar Imagem (opcional)", type=["png", "jpg", "jpeg"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📨 Enviar Demanda"):
            imagem_bytes = imagem.read() if imagem else None
            nome_imagem = imagem.name if imagem else None
            usuario_email = st.session_state.get("email", "anonimo@exemplo.com")
            salvar_demanda(titulo, descricao, categoria, nome_imagem)
            st.success("✅ Sua demanda foi enviada com sucesso para o feed!")
            st.balloons()
            st.session_state["pagina"] = "feed"

    with col2:
        if st.button("❌ Cancelar"):
            st.session_state["pagina"] = "feed"

    menu_inferior()

# ----------------------------
# PARTE 3: Visualizar demandas filtradas por categoria
# ----------------------------
def visualizar_por_categoria():
    categoria = st.session_state.get("categoria_selecionada", "Categoria")
    st.title(f"📌 Demandas: {categoria}")

    demandas = buscar_demandas_por_categoria(categoria)

    if not demandas:
        st.info("Nenhuma demanda cadastrada nesta categoria ainda.")
        return

    for titulo, descricao, nome_imagem in demandas:
        st.markdown(f"### {titulo}")
        st.write(descricao)
        if nome_imagem:
            st.markdown(f"*Imagem anexada: {nome_imagem}*")
        st.markdown("---")
    st.markdown("### teste")
    menu_inferior()

# ----------------------------
# PARTE 4: Página de perfil
# ----------------------------
def pagina_perfil():
    st.title("👤 Meu Perfil")

    st.image("perfil_padrao.png", width=120)  # imagem padrão

    nome = st.session_state.get("nome", "Nome não disponível")
    email = st.session_state.get("email", "Email não disponível")
    telefone = st.session_state.get("telefone", "Telefone não disponível")
    comunidade = st.session_state.get("comunidade", "Comunidade não disponível")
    senha = st.session_state.get("senha", "*******")

    st.markdown(f"**Nome:** {nome}")
    st.markdown(f"**Email:** {email}")
    st.markdown(f"**Telefone:** {telefone}")
    st.markdown(f"**Comunidade:** {comunidade}")
    st.markdown(f"**Senha:** {'●●●●●●' if senha else 'Não disponível'}")

    menu_inferior()
