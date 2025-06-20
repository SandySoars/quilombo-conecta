import sqlite3

def conectar():
    return sqlite3.connect("demandas.db")

def salvar_demanda(titulo, descricao, categoria, nome_imagem):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO demandas (titulo, descricao, categoria, nome_imagem)
        VALUES (?, ?, ?, ?)
    """, (titulo, descricao, categoria, nome_imagem))
    conn.commit()
    conn.close()

def buscar_demandas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, descricao, categoria, nome_imagem FROM demandas ORDER BY id DESC")
    demandas = cursor.fetchall()
    conn.close()
    return demandas

def buscar_demandas_por_categoria(categoria):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT titulo, descricao, nome_imagem FROM demandas
        WHERE categoria=?
        ORDER BY id DESC
    """, (categoria,))
    demandas = cursor.fetchall()
    conn.close()
    return demandas
