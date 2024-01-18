from models.toolkit.genericdatabasecrud import GenericDatabaseCRUD as CRUD

banco = CRUD(
    db_name='minha_loja.db',
    db_user='admin',
    db_pass='12345'
)

banco.create(table_name='clientes', sql_query="""
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         nome TEXT NOT NULL,
         telefone TEXT NOT NULL UNIQUE,
         endereço TEXT NOT NULL, 
         e_mail TEXT UNIQUE NOT NULL

""")






