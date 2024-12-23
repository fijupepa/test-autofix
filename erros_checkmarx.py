import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Problema 1: Exposição de credenciais
# Credenciais hardcoded
DB_PASSWORD = "supersecretpassword"

# Problema 2: Comando de sistema vulnerável à injeção
ALLOWED_COMMANDS = {
    "list": "ls",
    "status": "stat"
}

@app.route("/run", methods=["POST"])
def run_command():
    user_input = request.form.get("command")
    # Valida o comando recebido do usuário
    if user_input in ALLOWED_COMMANDS:
        command = ALLOWED_COMMANDS[user_input]
        result = subprocess.check_output(command, shell=True)
        return result
    else:
        return "Comando não permitido", 400

# Problema 3: Validação inadequada de entrada do usuário
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    # Consulta SQL vulnerável a injeção
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '<password>'"
    print("Executing query:", query)
    # Simulação de execução (não use em produção)
    return "Query executed!"

# Problema 4: Manipulação insegura de arquivos
@app.route("/read", methods=["POST"])
def read_file():
    filename = request.form.get("filename")
    # Define a safe root directory
    safe_root = "/safe/directory"
    # Normalize the path and check if it is within the safe root directory
    fullpath = os.path.normpath(os.path.join(safe_root, filename))
    if not fullpath.startswith(safe_root):
        return "Access denied: Invalid file path", 400
    # Open the file if the path is valid
    with open(fullpath, "r") as file:
        data = file.read()
    return data

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "t")
    app.run(debug=debug_mode)
