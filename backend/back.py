import sqlite3

def create():
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(uid VARCHAR(8) PRIMARY KEY, pass VARCHAR, mobile NUMBER, address VARCHAR(50))")
    conn.commit()
    conn.close()

def insert(username,password,mobile,address):
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO customer VALUES(?,?,?,?)",(username,password,mobile,address))
    conn.commit()
    conn.close()

def create2():
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS orders(order_id INTEGER PRIMARY KEY, uid VARCHAR(8), details VARCHAR(50), sum INTEGER, FOREIGN KEY (uid) REFERENCES customer(uid))")
    conn.commit()
    conn.close()

def insert2(username,details,sum):
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO orders VALUES(NULL,'"+username+"','"+details+"',"+str(sum)+")")
    conn.commit()
    conn.close()

def delete(username):
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM customer WHERE uid=?",(username,))
    conn.commit()
    conn.close()

def view(username):
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM customer WHERE uid=?",(username,))
    rows=cur.fetchall()
    conn.close()
    return rows

def validate():
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("SELECT uid,pass FROM customer")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(username):
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM orders WHERE uid=?",(username,))
    rows=cur.fetchall()
    conn.close()
    return rows

def update(username,password,mobile,address):
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("UPDATE customer SET pass=?, mobile=?, address=? WHERE uid=?",(password,mobile,address,username))
    conn.commit()
    conn.close()
