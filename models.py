from pony.orm import Database, Required, PrimaryKey,Set,Optional

db = Database()

class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    alibaba_guranteed = Required(bool)
    certifications = Required(str)
    minimum_to_order = Required(int)
    ordered_or_sold = Required(int)
    supplier = Required('Supplier')
    min_price = Required(float)
    max_price = Required(float)

class Supplier(db.Entity):
    id = PrimaryKey(int, auto=True)
    products = Set('Product')
    name = Required(str)
    verification_mode = Required(str)
    sopi_level = Required(int)
    country_name = Optional(str)
    years_as_gold_supplier = Required(int)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)