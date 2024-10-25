import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_STORE)
    cursor.execute(queries.CREATE_TABLE_DETAIL_STORE)
    cursor.execute(queries.CREATE_TABLE_COLLECTION_PRODUCTS)


async def sql_insert_store(name_product, product_id, size, price, photo):
    cursor.execute(queries.INSERT_STORE_QUERY, (
        name_product, product_id, size, price, photo
    ))
    db.commit()
async def sql_insert_store_detail(product_id, category, info_product):
    cursor.execute(queries.INSERT_DETAIL_STORE, (
        product_id, category, info_product
    ))
    db.commit()
async def sql_insert_collection(product_id, collection):
    cursor.execute(queries.INSERT_COLLECTION, (
        product_id, collection
    ))
    db.commit()