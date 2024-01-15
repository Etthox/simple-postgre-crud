import psycopg2


conn = psycopg2.connect(dbname="postgres", user="postgres", password="26673108rod", port="5432")
cur = conn.cursor()


def create():
    cur.execute('''CREATE TABLE student(Id SERIAL, Name Text, Age TEXT, Address TEXT);''')
    print("table created")
    conn.commit()
    conn.close()

def insert():
    cur.execute('''INSERT INTO student(Name, Age, Address) VALUES ('JOHN', '22', 'LUIS ROSANOVA 118');''')
    print("table created")
    conn.commit()
    conn.close()

def delete():
    cur.execute('''delete from student where id = 1;''')
    print("deleted successfully")
    conn.commit()
    conn.close()

def update():
    cur.execute('''update student set Age = '23' where (id) = (2);''')
    print("updated successfully")
    conn.commit()
    conn.close()


delete()

