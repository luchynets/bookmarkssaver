import psycopg2


class DataBase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database="bkmanager",
                user="postgres",
                password="1111",
                host="localhost",
                port="5432"
            )
            print("Connection to the PostgreSQL database successful.")
        except psycopg2.DatabaseError as e:
            print(f"An error occurred: {e}")

    def bk_get(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM bookmark')
            rows = cursor.fetchall()
            data = {'bookmarks': []}
            for row in rows:
                cursor.execute('SELECT category_name FROM category WHERE category_id=%s', (row[3], ))
                type = cursor.fetchone()[0]
                data['bookmarks'].append({'bk_id': row[0], 'bk_name': row[1], 'bk_url': row[2], 'bk_category': type, 'ct_id': row[3]})
            return data

    def catgrs_get(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM category')
            rows = cursor.fetchall()
            data = {'categories': []}
            for row in rows:
                data['categories'].append({'ct_id': row[0], 'ct_name': row[1]})
            return data

    def bk_get_by_id(self, id):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM bookmark WHERE bookmark_id=%s', (id, ))
            rows = cursor.fetchall()
            data = {'bookmark': []}
            for row in rows:
                cursor.execute('SELECT category_name FROM category WHERE category_id=%s', (row[3], ))
                type = cursor.fetchone()[0]
                data['bookmark'].append({'bk_id': row[0], 'bk_name': row[1], 'bk_url': row[2], 'bk_category': type})
            return data

    def add_bk(self, name, url, type):
        with self.conn.cursor() as cursor:
            cursor.execute('INSERT INTO bookmark (bk_name, bk_url, bk_type) VALUES (%s, %s, %s) RETURNING bookmark_id', (name, url, type))
            id_ = cursor.fetchone()[0]
            self.conn.commit()
            return {'response': 'New bookmark has been added.', 'bookmark_id': id_}

    def add_category(self, name):
        with self.conn.cursor() as cursor:
            cursor.execute('INSERT INTO category (category_name) VALUES (%s) RETURNING category_id', (name,))
            id_ = cursor.fetchone()[0]
            self.conn.commit()
            return {'response': 'Category has been added.', 'category_id': id_}
