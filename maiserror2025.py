import os
import subprocess
import requests
import jwt  # PyJWT

# 1. Hardcoded secret
JWT_SECRET = "123456"  # CWE-798: Use of Hard-coded Credentials

# 2. SQL Injection
def get_user_info(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"  # CWE-89
    print("Executing query:", query)
    # Suponha que estamos passando essa query para algum banco inseguro...

# 3. Command Injection
def list_files(directory):
    subprocess.call(f"ls {directory}", shell=True)  # CWE-78

# 4. Deserialização insegura
import pickle
def load_data(data):
    return pickle.loads(data)  # CWE-502

# 5. Exposição de informações sensíveis via logs
def login(user, password):
    print(f"Usuário: {user}, Senha: {password}")  # CWE-532

# 6. Download inseguro de conteúdo externo
def fetch_remote_file(url):
    response = requests.get(url)
    with open("file.txt", "w") as f:
        f.write(response.text)  # CWE-494

# 7. Uso inseguro de JWT sem validação de assinatura
def decode_token(token):
    return jwt.decode(token, options={"verify_signature": False})  # CWE-345

# 8. Falta de verificação de certificado SSL
def get_data_from_insecure_site():
    response = requests.get("https://inseguro.exemplo.com", verify=False)  # CWE-295
    return response.text

# 9. Permissões excessivas de arquivos
def create_config_file():
    with open("config.txt", "w") as f:
        f.write("configuracao=valor")
    os.chmod("config.txt", 0o777)  # CWE-732

# 10. Validação de entrada ausente (XSS simulada via web API)
def render_name(name):
    return f"<html><body>Olá {name}</body></html>"  # CWE-79
