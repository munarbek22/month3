CREATE_TABLE_STORE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    product_id VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    photo TEXT
    )
"""

INSERT_STORE_QUERY = """
    INSERT INTO store (name_product, product_id, size, price, photo)
    VALUES (?, ?, ?, ?, ?)
"""
CREATE_TABLE_STORE_DETAIL = """
CREATE TABLE IF NOT EXISTS detail_store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(255),
    category VARCHAR(255),
    info_product VARCHAR(255)
    )
 """

CREATE_TABLE_COLLECTION_PRODUCTS = """
CREATE TABLE IF NOT EXISTS collection_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(255),
    collection VARCHAR(255)
)
"""

INSERT_COLLECTION = """
    INSERT INTO collection_products(product_id, collection)
    VALUES(?, ?)
"""