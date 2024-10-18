import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_STORE)

async def sql_insert_store(name, size, price, photo, product_id):
    cursor.execute(queries.INSERT_VALUES, (
        name, size, price, photo, product_id
    ))

async def sql_create_table():
    cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAILS)

async def sql_insert_product_details(product_id, category, info_product):
    cursor.execute(queries.INSERT_IN_DETAILS, (
        product_id, category, info_product
    ))

    db.commit()