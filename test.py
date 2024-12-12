string = '123456 67890123 1283791263 127361 12937123 12837 123843'

lista = string.split(" ")
print(lista)

print(f"chunck quantities are {len(lista)}")
print('')
def tamanho_lista(param):
    for pedaco in param:
        if len(pedaco) != 6:
            print(pedaco)

tamanho_lista(lista)


app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)")
    return conn

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM user WHERE id = {user_id}")