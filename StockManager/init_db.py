import sqlite3


if __name__ == '__main__':

    conn = sqlite3.connect('stock.db')

    c = conn.cursor()


    c.execute("""CREATE TABLE stock (
                name text,
                quantity integer,
                cost integer
                ) """)

    conn.commit()
