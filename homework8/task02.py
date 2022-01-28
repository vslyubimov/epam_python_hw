"""
Write a wrapper class TableData for database table, that when initialized
with database name and table acts as collection object
(implements Collection protocol). Assume all data has unique values
in 'name' column. So,
if presidents = TableData(database_name='example.sqlite',
                            table_name='presidents')

then

len(presidents) will give current amount of rows
in presidents table in database
presidents['Yeltsin'] should return single data
row for president with name Yeltsin
'Yeltsin' in presidents should return if president
with same name exists in table
object implements iteration protocol. i.e.
you could use it in for loops::

    for president in presidents:
        print(president['name'])
all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance,
your calls should return updated data.
Avoid reading entire table into memory. When iterating through records,
start reading the first record, then go to the next one,
until records are exhausted. When writing tests, it's not always neccessary
to mock database calls completely. Use supplied example.sqlite file
as database fixture file.
"""

import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.table_name = table_name
        self.database_name = database_name

    def __len__(self) -> int:
        self._cursor.execute(f"select count(*) from {self.table_name}")
        return self._cursor.fetchone()[0]

    def __getitem__(self, item: str):
        _sql_call = f"SELECT * from {self.table_name} where name=:name"
        self._cursor.execute(_sql_call, {"name": item})
        return dict(self._cursor.fetchone())

    def __iter__(self):
        for row in self._cursor.execute(f"SELECT * from {self.table_name}"):
            yield dict(row)

    def __contains__(self, item: str) -> bool:
        _sql_call = \
            f"SELECT EXISTS(SELECT 1 from {self.table_name} where name=:name)"
        self._cursor.execute(_sql_call, {"name": item})
        return self._cursor.fetchone()[0]

    def __enter__(self):
        self._conn = sqlite3.connect(self.database_name)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
