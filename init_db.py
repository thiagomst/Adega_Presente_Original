import sqlite3
from werkzeug.security import generate_password_hash

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('adega.db')
    conn.row_factory = sqlite3.Row  # Retorna as linhas como dicionários
    return conn

try:
    # Conectar ao banco de dados (ou criar se não existir)
    conn = get_db_connection()
    c = conn.cursor()

    # Criar tabela de vinhos com a coluna 'imagem' e 'descricao'
    c.execute('''
        CREATE TABLE IF NOT EXISTS vinhos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            imagem TEXT NOT NULL,
            descricao TEXT  -- Nova coluna
        )
    ''')
    print("Tabela 'vinhos' criada com sucesso ou já existente.")

    # Inserir alguns vinhos de exemplo com caminhos de imagens e descrições
    vinhos_exemplo = [
        ('Vinho Tinto', 50.00, 'vinho_tinto.jpg', 'Um vinho tinto encorpado com notas de frutas vermelhas.'),
        ('Vinho Branco', 40.00, 'vinho_branco.jpg', 'Um vinho branco leve e refrescante.'),
        ('Vinho Rosé', 35.00, 'vinho_rose.jpg', 'Um vinho rosé suave e frutado.')
    ]
    c.executemany("INSERT INTO vinhos (nome, preco, imagem, descricao) VALUES (?, ?, ?, ?)", vinhos_exemplo)
    print("Vinhos de exemplo inseridos com sucesso.")

    # Criar tabela de usuários com o campo 'role'
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user',  -- Campo para definir o papel do usuário
            imagem BLOB  -- Nova coluna para salvar imagens
        )
    ''')
    print("Tabela 'usuarios' criada com sucesso ou já existente.")

    # Inserir alguns usuários de exemplo, incluindo um admin
    usuarios_exemplo = [
        ('admin', generate_password_hash('admin123'), 'admin'),
        ('user1', generate_password_hash('user123'), 'user'),
        ('user2', generate_password_hash('user456'), 'user')
    ]
    c.executemany("INSERT INTO usuarios (username, password, role) VALUES (?, ?, ?)", usuarios_exemplo)
    print("Usuários de exemplo inseridos com sucesso.")

    conn.commit()

except sqlite3.Error as e:
    print(f"Erro ao acessar o banco de dados: {e}")

finally:
    if conn:
        conn.close()
        print("Conexão com o banco de dados fechada.")