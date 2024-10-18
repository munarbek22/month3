CREATE_TABLE_STORE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    photo TEXT
    )
"""

INSERT_VALUES = """
    INSERT INTO store(name, size, price, photo)
    VALUES (?, ?, ?, ?)
"""




CREATE_TABLE_PRODUCTS_DETAILS = """
CREATE TABLE IF NOT EXISTS products_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid INTEGER NOT NULL,
    category VARCHAR(255),
    infoproduct TEXT
)
"""

INSERT_STORE = """
    INSERT INTO store(product_id)
    VALUES (?)
"""

INSERT_IN_DETAILS = """
    INSERT INTO product_details(product_id, category, info_product)
    VALUES (?, ?, ?)
"""