import sqlite3
import streamlit as st

def conectar():
    return sqlite3.connect("demandas.db")

def cadastrar_user(nome, email, telefone, senha, comunidade):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuarios (nome, email, telefone, senha, comunidade)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, email, telefone, senha, comunidade))
        conn.commit()

        # Salva no session_state
        st.session_state["usuario_logado"] = True
        st.session_state["nome"] = nome
        st.session_state["email"] = email
        st.session_state["telefone"] = telefone
        st.session_state["senha"] = senha
        st.session_state["comunidade"] = comunidade
        st.success("✅ Cadastro realizado com sucesso!")

    except sqlite3.IntegrityError:
        st.error("❌ Este e-mail já está cadastrado.")
    finally:
        conn.close()

def login_user(email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, telefone, comunidade FROM usuarios WHERE email=? AND senha=?", (email, senha))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        nome, telefone, comunidade = resultado
        st.session_state["usuario_logado"] = True
        st.session_state["nome"] = nome
        st.session_state["email"] = email
        st.session_state["telefone"] = telefone
        st.session_state["senha"] = senha
        st.session_state["comunidade"] = comunidade
        st.success(f"🔓 Bem-vindo(a), {nome}!")
    else:
        st.error("❌ Email ou senha incorretos.")
