"""
2) Написать класс обаработчик, который принимает имя таблицы в БД,
и путь до json файла.
Если таблицы нет - создает ее, парсит json и добавляет записи в таблицу.
Объекты внутри json файла могут содержать разное количество полей,
однако в базу нужно добавить все, если какого-то поля нет - добавить None.
Обязательные поля: [first_name, last_name, date_of_bd].
Если какого-то поля нет, выдавать в stderr этот объект
(в базу он попасть не должен).
(ORM не обязательна)
По возможности распараллелить работу
"""

import json
import sqlite3
import sys

types = {
    'int': "INTEGER",
    'float': "REAL",
    'str': "TEXT"
}


class Handler:
    def __init__(self, database, json_path):
        self.database = database
        self.json_path = json_path
        self.json_data = None
        self.must_have_columns = set(['first_name', 'last_name', 'date_of_db'])

    def create_db(self):  # создает db, если check_db_exist is false
        self._conn = sqlite3.connect(self.database)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()

    def read_json(self):  # json_data из json
        with open(self.json_path) as js:
            self.json_data = json.load(js)

    # in fill_db
    def create_table(self, table_name):  # тейблы из json
        columns_with_types = ",".join([f'{column} TEXT NOT NULL' for column in self.must_have_columns])
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});")

    # in fill_db
    def alter_table(self, table_name, columns, columns_types):  # добавление столбцов и типов
        for column, type_ in zip(columns, columns_types):
            self._cursor.execute(f"ALTER TABLE {table_name} ADD {column} {types[type_]};")

    def read_table_columns(self, table_name):
        columns = self._cursor.execute(f"SELECT name FROM pragma_table_info('{table_name}')").fetchall()
        return set([x[0] for x in columns])

    def fill_db(self):  # добавление данных по столбцам
        for table_name, table_content in self.json_data.items():
            self.create_table(table_name)
            current_table_columns = self.read_table_columns(table_name) or self.must_have_columns.copy()
            for card in table_content:
                if self.must_have_columns.issubset(set(card.keys())):  # есть базовые поля
                    column_must_add = set(card.keys()) - current_table_columns  # определяем, разницу столбцов
                    if column_must_add:
                        # types
                        column_types = [
                            type(value).__name__ for header, value in card.items() if header in column_must_add
                        ]

                        self.alter_table(table_name, column_must_add, column_types)  # добавляем недостающие столбцы
                        current_table_columns = current_table_columns.union(column_must_add)

                    values = ','.join([f'\'{x}\'' if isinstance(x, str) else str(x) for x in card.values()])
                    # сформировали values
                    self._cursor.execute(f"INSERT INTO {table_name} ({','.join(card.keys())}) \
                        VALUES ({values});")  # заполнили

                else:
                    print(card, file=sys.stderr)

    def close_conn(self):
        self._conn.commit()
        self._conn.close()

    def __call__(self):
        self.create_db()
        self.read_json()
        self.fill_db()
        self.close_conn()
        # парсит json, добавляет в db


if __name__ == '__main__':
    handler = Handler('from_json.sqlite', 'testfile.json')
    handler()
