from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_from_directory
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui_mais_segura_e_unica'  # Use uma chave secreta forte

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('adega.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/img/hero/<filename>')
def serve_image(filename):
    return send_from_directory('static/img/hero', filename)


@app.route('/')
def index():
    imagens = [
        'hero-1.jpg',
        'hero-2.jpg',
        'hero-3.jpg'
    ]
    return render_template('index.html', imagens=imagens)

@app.route('/espumantes')
def espumantes():
    return render_template('espumantes.html')

@app.route('/vinho_branco')
def vinho_branco():
    return render_template('vinho_branco.html')

@app.route('/vinho_rose')
def vinho_rose():
    return render_template('vinho_rose.html')

@app.route('/vinho_tinto')
def vinho_tinto():
    return render_template('vinho_tinto.html')

@app.route('/embalagens')
def embalagens():
    return render_template('embalagens.html')

@app.route('/novidades')
def novidades():
    return render_template('novidades.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)