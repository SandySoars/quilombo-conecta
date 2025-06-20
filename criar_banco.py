import sqlite3

conn = sqlite3.connect("demandas.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS demandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    categoria TEXT NOT NULL,
    nome_imagem TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    telefone TEXT,
    senha TEXT NOT NULL,
    comunidade TEXT
)
""")

conn.commit()
conn.close()

print("✅ Banco de dados 'demandas.db' criado com sucesso!")
