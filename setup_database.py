import sqlite3

database_con = sqlite3.connect("bank.db")
cursor = database_con.cursor()

def setup_db_tables():
    sql_statements = [
        
    """CREATE TABLE IF NOT EXISTS user(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   idnumber TEXT NOT NULL
                   );""",
    
    """CREATE TABLE IF NOT EXISTS address( 
                   id INTEGER PRIMARY KEY NOT NULL,
                   user_id INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   street TEXT NOT NULL,
                   number TEXT,
                   neighbornhood TEXT NOT NULL,
                   district TEXT NOT NULL,
                   city TEXT NOT NULL,
                   FOREIGN KEY(user_id) references user(id)
                   );""",
    
    """CREATE TABLE IF NOT EXISTS account(
                   id INTEGER PRIMARY KEY,
                   user_id INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   account_number TEXT NOT NULL,
                   FOREIGN KEY(user_id) references user(id)
                   );"""
    ]
    try:
        with sqlite3.connect("bank.db") as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            
            conn.commit()
    except sqlite3.Error as e:
        print(e)
   

if __name__ == '__main__':
    setup_db_tables()