import sqlite3

connection = sqlite3.connect('.\Inventario Planta Física\db.sqlite3')

cursor = connection.cursor()

cursor.execute('SELECT * FROM store_order')

rows = cursor.fetchall()

print(rows)

def get_quantity(barcode):

    product_id = cursor.execute('SELECT id FROM inventory_product WHERE barcode = ?', (barcode,)).fetchone()[0]
    quantity = 0
    cursor.execute('SELECT quantity, order_id FROM store_orderdetail WHERE product_id = ?', (product_id,))
    product_orders = cursor.fetchall()
    for product_order in product_orders:
        cursor.execute('SELECT type FROM store_order WHERE id = ?', (product_order[1],))
        order_type = cursor.fetchone()
        if order_type[0] == 'I':
            quantity += product_order[0]
        else:
            quantity -= product_order[0]

    return quantity
