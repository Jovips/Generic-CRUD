# Generic-CRUD
CRUD Genérico em Python com SQLite

## Requirements
Make sure you have Python installed on your machine. Additionally, you can install the dependencies using the following command:
```bash
pip install sqlite3

```
## About CRUD
The generic CRUD provides the basic operations of creating, reading, updating, and deleting records. 
### Example of use:
```bash
from models.toolkit.genericdatabasecrud import GenericDatabaseCRUD as CRUD

banco = CRUD(
    db_name='your_database.db',
    db_user='your_user',
    db_pass='your_password'
)

banco.create(table_name='exemplo', sql_query="""
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         nome TEXT NOT NULL,
         telefone TEXT NOT NULL UNIQUE,
         endereço TEXT NOT NULL, 
         e_mail TEXT UNIQUE NOT NULL

""")

```

## Contributions
Contributions are welcome! Feel free to open issues or pull requests.
